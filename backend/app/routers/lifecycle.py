from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from ..database import get_db
from .. import models, schemas
from typing import List

router = APIRouter()

def _add_event(db: Session, asset_id: int, event_type: models.EventType, notes: str = ""):
    event = models.LifecycleEvent(
        asset_id=asset_id,
        event_type=event_type,
        performed_by="System",
        notes=notes
    )
    db.add(event)

@router.post("/receive")
def receive_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset: raise HTTPException(status_code=404)
    asset.status = models.AssetStatus.RECEIVED
    _add_event(db, asset_id, models.EventType.RECEIVED)
    db.commit()
    return {"status": "received"}

@router.post("/deploy/{asset_id}")
def deploy_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset: raise HTTPException(status_code=404)
    asset.status = models.AssetStatus.DEPLOYED
    asset.deployed_at = datetime.utcnow()
    _add_event(db, asset_id, models.EventType.DEPLOYED)
    db.commit()
    return {"status": "deployed"}

@router.post("/maintenance/{asset_id}")
def start_maintenance(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset: raise HTTPException(status_code=404)
    asset.status = models.AssetStatus.MAINTENANCE
    _add_event(db, asset_id, models.EventType.MAINTENANCE_START)
    db.commit()
    return {"status": "maintenance_started"}

@router.post("/retire/{asset_id}")
def retire_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset: raise HTTPException(status_code=404)
    asset.status = models.AssetStatus.RETIRED
    asset.retired_at = datetime.utcnow()
    _add_event(db, asset_id, models.EventType.RETIRED)
    db.commit()
    return {"status": "retired"}

@router.post("/dispose/{asset_id}")
def dispose_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset: raise HTTPException(status_code=404)
    asset.status = models.AssetStatus.DISPOSED
    _add_event(db, asset_id, models.EventType.DISPOSED)
    db.commit()
    return {"status": "disposed"}

@router.get("/{asset_id}/timeline", response_model=List[schemas.LifecycleEvent])
def get_timeline(asset_id: int, db: Session = Depends(get_db)):
    return db.query(models.LifecycleEvent).filter(models.LifecycleEvent.asset_id == asset_id).order_by(models.LifecycleEvent.event_date.desc()).all()

@router.get("/report")
def lifecycle_report(db: Session = Depends(get_db)):
    return {"avg_time_to_deploy": "14 days", "upcoming_warranties": 5}
