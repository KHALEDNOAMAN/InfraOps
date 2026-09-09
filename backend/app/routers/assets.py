from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from .. import models, schemas
from sqlalchemy import or_

router = APIRouter()

@router.get("/", response_model=List[schemas.Asset])
def list_assets(
    type: Optional[models.AssetType] = None,
    status: Optional[models.AssetStatus] = None,
    datacenter: Optional[int] = None,
    rack: Optional[int] = None,
    db: Session = Depends(get_db)
):
    q = db.query(models.Asset)
    if type: q = q.filter(models.Asset.asset_type == type)
    if status: q = q.filter(models.Asset.status == status)
    if rack: q = q.filter(models.Asset.rack_id == rack)
    return q.all()

@router.post("/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(models.Asset).count()
    deployed = db.query(models.Asset).filter(models.Asset.status == models.AssetStatus.DEPLOYED).count()
    return {"total_assets": total, "deployed": deployed}

@router.get("/search", response_model=List[schemas.Asset])
def search_assets(q: str, db: Session = Depends(get_db)):
    return db.query(models.Asset).filter(
        or_(
            models.Asset.hostname.ilike(f"%{q}%"),
            models.Asset.ip_address.ilike(f"%{q}%"),
            models.Asset.serial_number.ilike(f"%{q}%"),
            models.Asset.asset_tag.ilike(f"%{q}%")
        )
    ).all()

@router.get("/{id}", response_model=schemas.Asset)
def get_asset(id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == id).first()
    if not asset:
        raise HTTPException(status_code=404)
    return asset

@router.patch("/{id}", response_model=schemas.Asset)
def update_asset(id: int, asset_data: dict, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == id).first()
    if not asset: raise HTTPException(status_code=404)
    for key, val in asset_data.items():
        setattr(asset, key, val)
    db.commit()
    db.refresh(asset)
    return asset

@router.post("/{id}/assign-rack")
def assign_rack(id: int, rack_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == id).first()
    if not asset: raise HTTPException(status_code=404)
    asset.rack_id = rack_id
    db.commit()
    return {"status": "success"}

@router.get("/{id}/vms", response_model=List[schemas.VMInstance])
def get_vms(id: int, db: Session = Depends(get_db)):
    return db.query(models.VMInstance).filter(models.VMInstance.host_asset_id == id).all()

@router.post("/{id}/vms", response_model=schemas.VMInstance)
def create_vm(id: int, vm: schemas.VMInstanceCreate, db: Session = Depends(get_db)):
    db_vm = models.VMInstance(**vm.dict())
    db_vm.host_asset_id = id
    db.add(db_vm)
    db.commit()
    db.refresh(db_vm)
    return db_vm
