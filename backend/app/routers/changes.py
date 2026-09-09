from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from ..database import get_db
from .. import models, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.ChangeRequest])
def list_changes(db: Session = Depends(get_db)):
    return db.query(models.ChangeRequest).all()

@router.post("/", response_model=schemas.ChangeRequest)
def create_change(cr: schemas.ChangeRequestCreate, db: Session = Depends(get_db)):
    db_cr = models.ChangeRequest(**cr.dict())
    db.add(db_cr)
    db.commit()
    db.refresh(db_cr)
    return db_cr

@router.patch("/{id}/approve")
def approve_change(id: int, approver: str, db: Session = Depends(get_db)):
    cr = db.query(models.ChangeRequest).filter(models.ChangeRequest.id == id).first()
    if not cr: raise HTTPException(status_code=404)
    cr.status = models.ChangeStatus.APPROVED
    cr.approver = approver
    db.commit()
    return {"status": "approved"}

@router.patch("/{id}/reject")
def reject_change(id: int, reason: str, db: Session = Depends(get_db)):
    cr = db.query(models.ChangeRequest).filter(models.ChangeRequest.id == id).first()
    if not cr: raise HTTPException(status_code=404)
    cr.status = models.ChangeStatus.REJECTED
    cr.approval_notes = reason
    db.commit()
    return {"status": "rejected"}

@router.patch("/{id}/start")
def start_change(id: int, db: Session = Depends(get_db)):
    cr = db.query(models.ChangeRequest).filter(models.ChangeRequest.id == id).first()
    if not cr: raise HTTPException(status_code=404)
    cr.status = models.ChangeStatus.IN_PROGRESS
    db.commit()
    return {"status": "started"}

@router.patch("/{id}/complete")
def complete_change(id: int, db: Session = Depends(get_db)):
    cr = db.query(models.ChangeRequest).filter(models.ChangeRequest.id == id).first()
    if not cr: raise HTTPException(status_code=404)
    cr.status = models.ChangeStatus.COMPLETED
    cr.completed_date = datetime.utcnow()
    db.commit()
    return {"status": "completed"}

@router.patch("/{id}/rollback")
def rollback_change(id: int, db: Session = Depends(get_db)):
    cr = db.query(models.ChangeRequest).filter(models.ChangeRequest.id == id).first()
    if not cr: raise HTTPException(status_code=404)
    cr.status = models.ChangeStatus.ROLLBACK
    db.commit()
    return {"status": "rolled_back"}

@router.get("/calendar")
def get_calendar(db: Session = Depends(get_db)):
    changes = db.query(models.ChangeRequest).filter(models.ChangeRequest.scheduled_date != None).all()
    return [{"id": c.id, "title": c.title, "date": c.scheduled_date} for c in changes]
