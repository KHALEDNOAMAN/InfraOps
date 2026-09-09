from sqlalchemy.orm import Session
from .. import models
import random

def calculate_utilization(db: Session, datacenter_id: int):
    # Dummy logic for utilization
    return {
        "datacenter_id": datacenter_id,
        "cpu_usage_pct": 65.5,
        "ram_usage_pct": 72.1,
        "storage_usage_pct": 80.0,
        "power_usage_pct": 55.2
    }

def forecast_growth(db: Session, datacenter_id: int, resource: models.ResourceType):
    # Dummy linear regression results
    return {
        "datacenter_id": datacenter_id,
        "resource": resource,
        "current_usage_pct": 72.1,
        "predicted_usage_pct": 85.0,
        "days_until_80_pct": 45,
        "days_until_full": 120
    }

def recommend_placement(db: Session, asset_type: str, required_units: int, required_power: float):
    return {"recommended_racks": [1, 2, 5]}

def check_power_budget(db: Session, rack_id: int):
    rack = db.query(models.Rack).filter(models.Rack.id == rack_id).first()
    if rack:
        return rack.power_capacity_w - rack.current_power_w
    return 0.0

def generate_capacity_report(db: Session):
    return {"status": "generated", "report_url": "/reports/capacity_latest.pdf"}
