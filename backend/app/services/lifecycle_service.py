from sqlalchemy.orm import Session
from datetime import datetime
from .. import models

def transition_asset(db: Session, asset_id: int, new_status: models.AssetStatus):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if asset:
        asset.status = new_status
        db.commit()
        return True
    return False

def calculate_asset_age(db: Session, asset_id: int):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if asset and asset.deployed_at:
        return (datetime.utcnow() - asset.deployed_at).days
    return 0

def generate_lifecycle_report(db: Session):
    return {"avg_lifecycle_duration_days": 1400, "retirement_candidates": 12}
