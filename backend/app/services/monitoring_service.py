from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from .. import models

def collect_rack_metrics(db: Session, rack_id: int):
    return {"power_watts": 3500.0, "temperature_c": 22.5, "humidity_pct": 45.0}

def check_warranty_expiry(db: Session):
    now = datetime.utcnow()
    in_30_days = now + timedelta(days=30)
    assets = db.query(models.Asset).filter(models.Asset.warranty_expires <= in_30_days).all()
    return [{"asset_id": a.id, "expires": a.warranty_expires} for a in assets]

def detect_anomalies(db: Session, rack_id: int):
    # Dummy anomaly detection logic
    return {"rack_id": rack_id, "anomalies": ["Temperature spike detected 2 hours ago."]}
