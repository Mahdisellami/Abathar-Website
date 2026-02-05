from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class EventBase(BaseModel):
    """Base schema for Event"""
    title: str = Field(..., min_length=1, max_length=500)
    date: date
    time: Optional[str] = Field(None, max_length=50)
    venue: str = Field(..., min_length=1, max_length=255)
    location: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    ensemble_name: Optional[str] = Field(None, max_length=255)
    event_type: Optional[str] = Field(None, max_length=100)
    is_past: bool = False


class EventCreate(EventBase):
    """Schema for creating a new event"""
    pass


class EventUpdate(BaseModel):
    """Schema for updating an event (all fields optional)"""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    date: Optional[date] = None
    time: Optional[str] = Field(None, max_length=50)
    venue: Optional[str] = Field(None, min_length=1, max_length=255)
    location: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    ensemble_name: Optional[str] = Field(None, max_length=255)
    event_type: Optional[str] = Field(None, max_length=100)
    is_past: Optional[bool] = None


class EventSchema(EventBase):
    """Schema for returning event data"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enables ORM mode for SQLAlchemy models
