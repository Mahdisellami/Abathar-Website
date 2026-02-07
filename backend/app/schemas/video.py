from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional


class VideoBase(BaseModel):
    """Base schema for Video"""
    title: str = Field(..., min_length=1, max_length=500)
    youtube_id: str = Field(..., min_length=1, max_length=50)
    youtube_url: str = Field(..., min_length=1, max_length=500)
    description: Optional[str] = None
    thumbnail_url: Optional[str] = Field(None, max_length=500)
    duration: Optional[str] = Field(None, max_length=20)
    published_date: Optional[date] = None
    category: Optional[str] = Field(None, max_length=100)
    event_id: Optional[int] = None
    is_featured: bool = False
    display_order: int = 0
    is_visible: bool = True


class VideoCreate(VideoBase):
    """Schema for creating a new video"""
    pass


class VideoUpdate(BaseModel):
    """Schema for updating a video (all fields optional)"""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    youtube_id: Optional[str] = Field(None, min_length=1, max_length=50)
    youtube_url: Optional[str] = Field(None, min_length=1, max_length=500)
    description: Optional[str] = None
    thumbnail_url: Optional[str] = Field(None, max_length=500)
    duration: Optional[str] = Field(None, max_length=20)
    published_date: Optional[date] = None
    category: Optional[str] = Field(None, max_length=100)
    event_id: Optional[int] = None
    is_featured: Optional[bool] = None
    display_order: Optional[int] = None
    is_visible: Optional[bool] = None


class VideoSchema(VideoBase):
    """Schema for returning video data"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enables ORM mode for SQLAlchemy models
