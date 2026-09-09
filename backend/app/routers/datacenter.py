from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.DataCenter])
def list_datacenters(db: Session = Depends(get_db)):
    return db.query(models.DataCenter).all()

@router.post("/", response_model=schemas.DataCenter)
def create_datacenter(dc: schemas.DataCenterCreate, db: Session = Depends(get_db)):
    db_dc = models.DataCenter(**dc.dict())
    db.add(db_dc)
    db.commit()
    db.refresh(db_dc)
    return db_dc

@router.get("/{id}", response_model=schemas.DataCenter)
def get_datacenter(id: int, db: Session = Depends(get_db)):
    dc = db.query(models.DataCenter).filter(models.DataCenter.id == id).first()
    if not dc:
        raise HTTPException(status_code=404, detail="DataCenter not found")
    return dc

@router.get("/{id}/racks", response_model=List[schemas.Rack])
def get_racks(id: int, db: Session = Depends(get_db)):
    return db.query(models.Rack).filter(models.Rack.datacenter_id == id).all()

@router.post("/{id}/racks", response_model=schemas.Rack)
def add_rack(id: int, rack: schemas.RackCreate, db: Session = Depends(get_db)):
    db_rack = models.Rack(**rack.dict())
    db_rack.datacenter_id = id
    db.add(db_rack)
    db.commit()
    db.refresh(db_rack)
    return db_rack

@router.get("/{id}/floor-map")
def get_floor_map(id: int, db: Session = Depends(get_db)):
    racks = db.query(models.Rack).filter(models.Rack.datacenter_id == id).all()
    layout = []
    for r in racks:
        layout.append({
            "id": r.id,
            "name": r.name,
            "row": r.row_label,
            "position": r.position,
            "used_units": r.used_units,
            "total_units": r.total_units,
            "status": r.status
        })
    return {"datacenter_id": id, "layout": layout}

@router.get("/{id}/power-summary")
def get_power_summary(id: int, db: Session = Depends(get_db)):
    dc = db.query(models.DataCenter).filter(models.DataCenter.id == id).first()
    if not dc:
        raise HTTPException(status_code=404)
    racks = db.query(models.Rack).filter(models.Rack.datacenter_id == id).all()
    used_power = sum(r.current_power_w for r in racks) / 1000.0 # kw
    pue = 1.5 if used_power > 0 else 0.0 # dummy PUE
    return {
        "datacenter_id": id,
        "total_power_kw": dc.total_power_kw,
        "used_power_kw": used_power,
        "estimated_pue": pue
    }
