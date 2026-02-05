from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.bio import Bio
from ..schemas.bio import BioSchema, BioCreate, BioUpdate

router = APIRouter()


@router.get("/bio", response_model=BioSchema)
def get_bio(db: Session = Depends(get_db)):
    """
    Get the biography information.
    Returns the first (and typically only) bio entry.
    """
    bio = db.query(Bio).first()
    if not bio:
        raise HTTPException(status_code=404, detail="Biography not found")
    return bio


@router.post("/bio", response_model=BioSchema)
def create_bio(bio: BioCreate, db: Session = Depends(get_db)):
    """
    Create a new biography entry.
    (Typically used once during initial setup)
    """
    # Check if bio already exists
    existing_bio = db.query(Bio).first()
    if existing_bio:
        raise HTTPException(
            status_code=400,
            detail="Biography already exists. Use PUT to update."
        )

    db_bio = Bio(**bio.model_dump())
    db.add(db_bio)
    db.commit()
    db.refresh(db_bio)
    return db_bio


@router.put("/bio", response_model=BioSchema)
def update_bio(bio_update: BioUpdate, db: Session = Depends(get_db)):
    """
    Update the biography information.
    (Future admin feature)
    """
    bio = db.query(Bio).first()
    if not bio:
        raise HTTPException(status_code=404, detail="Biography not found")

    # Update only provided fields
    update_data = bio_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(bio, field, value)

    db.commit()
    db.refresh(bio)
    return bio


@router.delete("/bio/{bio_id}")
def delete_bio(bio_id: int, db: Session = Depends(get_db)):
    """
    Delete a biography entry.
    (Use with caution - typically not needed)
    """
    bio = db.query(Bio).filter(Bio.id == bio_id).first()
    if not bio:
        raise HTTPException(status_code=404, detail="Biography not found")

    db.delete(bio)
    db.commit()
    return {"message": "Biography deleted successfully"}
