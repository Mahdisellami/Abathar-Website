from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict, Any


class BioBase(BaseModel):
    """Base schema for Biography"""
    name: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=500)
    bio_text: str = Field(..., min_length=1)
    education: Optional[List[Dict[str, Any]]] = None
    achievements: Optional[List[Dict[str, Any]]] = None
    current_roles: Optional[List[Dict[str, Any]]] = None
    discography: Optional[List[Dict[str, Any]]] = None


class BioCreate(BioBase):
    """Schema for creating a new biography entry"""
    pass


class BioUpdate(BaseModel):
    """Schema for updating biography (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    bio_text: Optional[str] = Field(None, min_length=1)
    education: Optional[List[Dict[str, Any]]] = None
    achievements: Optional[List[Dict[str, Any]]] = None
    current_roles: Optional[List[Dict[str, Any]]] = None
    discography: Optional[List[Dict[str, Any]]] = None


class BioSchema(BioBase):
    """Schema for returning biography data"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enables ORM mode for SQLAlchemy models
