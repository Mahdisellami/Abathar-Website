from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.ensemble import Ensemble
from ..schemas.ensemble import EnsembleSchema, EnsembleCreate, EnsembleUpdate

router = APIRouter()


@router.get("/ensembles", response_model=List[EnsembleSchema])
def get_ensembles(db: Session = Depends(get_db)):
    """
    Get all ensembles.
    """
    ensembles = db.query(Ensemble).all()
    return ensembles


@router.get("/ensemble", response_model=EnsembleSchema)
def get_main_ensemble(db: Session = Depends(get_db)):
    """
    Get the main ensemble (Ogaro Ensemble).
    Returns the first ensemble entry.
    """
    ensemble = db.query(Ensemble).first()
    if not ensemble:
        raise HTTPException(status_code=404, detail="Ensemble not found")
    return ensemble


@router.get("/ensembles/{ensemble_id}", response_model=EnsembleSchema)
def get_ensemble_by_id(ensemble_id: int, db: Session = Depends(get_db)):
    """
    Get a specific ensemble by ID.
    """
    ensemble = db.query(Ensemble).filter(Ensemble.id == ensemble_id).first()
    if not ensemble:
        raise HTTPException(status_code=404, detail="Ensemble not found")
    return ensemble


@router.post("/ensembles", response_model=EnsembleSchema)
def create_ensemble(ensemble: EnsembleCreate, db: Session = Depends(get_db)):
    """
    Create a new ensemble.
    (Future admin feature)
    """
    # Check if ensemble with same name exists
    existing = db.query(Ensemble).filter(Ensemble.name == ensemble.name).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Ensemble '{ensemble.name}' already exists"
        )

    db_ensemble = Ensemble(**ensemble.model_dump())
    db.add(db_ensemble)
    db.commit()
    db.refresh(db_ensemble)
    return db_ensemble


@router.put("/ensemble", response_model=EnsembleSchema)
def update_main_ensemble(
    ensemble_update: EnsembleUpdate,
    db: Session = Depends(get_db)
):
    """
    Update the main ensemble information.
    (Future admin feature)
    """
    ensemble = db.query(Ensemble).first()
    if not ensemble:
        raise HTTPException(status_code=404, detail="Ensemble not found")

    # Update only provided fields
    update_data = ensemble_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(ensemble, field, value)

    db.commit()
    db.refresh(ensemble)
    return ensemble


@router.put("/ensembles/{ensemble_id}", response_model=EnsembleSchema)
def update_ensemble(
    ensemble_id: int,
    ensemble_update: EnsembleUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a specific ensemble by ID.
    (Future admin feature)
    """
    ensemble = db.query(Ensemble).filter(Ensemble.id == ensemble_id).first()
    if not ensemble:
        raise HTTPException(status_code=404, detail="Ensemble not found")

    # Update only provided fields
    update_data = ensemble_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(ensemble, field, value)

    db.commit()
    db.refresh(ensemble)
    return ensemble


@router.delete("/ensembles/{ensemble_id}")
def delete_ensemble(ensemble_id: int, db: Session = Depends(get_db)):
    """
    Delete an ensemble.
    (Use with caution)
    """
    ensemble = db.query(Ensemble).filter(Ensemble.id == ensemble_id).first()
    if not ensemble:
        raise HTTPException(status_code=404, detail="Ensemble not found")

    db.delete(ensemble)
    db.commit()
    return {"message": "Ensemble deleted successfully"}
