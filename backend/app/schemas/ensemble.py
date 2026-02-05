from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional, List, Dict, Any


class EnsembleBase(BaseModel):
    """Base schema for Ensemble"""
    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    formation_year: Optional[int] = Field(None, ge=1900, le=2100)
    musical_style: Optional[str] = None
    vision: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = Field(None, max_length=50)
    members: Optional[List[Dict[str, Any]]] = None
    highlights: Optional[List[Dict[str, Any]]] = None


class EnsembleCreate(EnsembleBase):
    """Schema for creating a new ensemble"""
    pass


class EnsembleUpdate(BaseModel):
    """Schema for updating an ensemble (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)
    formation_year: Optional[int] = Field(None, ge=1900, le=2100)
    musical_style: Optional[str] = None
    vision: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = Field(None, max_length=50)
    members: Optional[List[Dict[str, Any]]] = None
    highlights: Optional[List[Dict[str, Any]]] = None


class EnsembleSchema(EnsembleBase):
    """Schema for returning ensemble data"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enables ORM mode for SQLAlchemy models
