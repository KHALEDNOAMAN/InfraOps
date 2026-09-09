from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..services.capacity_service import calculate_utilization, forecast_growth

router = APIRouter()

@router.get("/overview")
def get_overview(datacenter_id: int, db: Session = Depends(get_db)):
    return calculate_utilization(db, datacenter_id)

@router.get("/racks/{id}")
def get_rack_capacity(id: int, db: Session = Depends(get_db)):
    rack = db.query(models.Rack).filter(models.Rack.id == id).first()
    if not rack:
        raise HTTPException(status_code=404)
    return {
        "id": rack.id,
        "u_space": {"total": rack.total_units, "used": rack.used_units, "free": rack.total_units - rack.used_units},
        "power": {"capacity_w": rack.power_capacity_w, "used_w": rack.current_power_w}
    }

@router.get("/forecast")
def get_forecast(datacenter_id: int, db: Session = Depends(get_db)):
    return forecast_growth(db, datacenter_id, models.ResourceType.POWER)

@router.get("/recommendations")
def get_recommendations(asset_type: str, units: int, power: float, db: Session = Depends(get_db)):
    racks = db.query(models.Rack).filter(models.Rack.status == models.RackStatus.ACTIVE).all()
    valid_racks = []
    for r in racks:
        if (r.total_units - r.used_units) >= units and (r.power_capacity_w - r.current_power_w) >= power:
            valid_racks.append(r.id)
    return {"recommended_rack_ids": valid_racks}

@router.get("/licenses")
def get_license_capacity(db: Session = Depends(get_db)):
    licenses = db.query(models.License).all()
    return [{"software": l.software_name, "total": l.seats, "used": l.used_seats} for l in licenses]

@router.get("/power-history")
def get_power_history(rack_id: int, db: Session = Depends(get_db)):
    readings = db.query(models.PowerReading).filter(models.PowerReading.rack_id == rack_id).order_by(models.PowerReading.recorded_at.desc()).limit(100).all()
    return readings
