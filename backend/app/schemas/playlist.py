"""
Playlist Schemas

Pydantic schemas for YouTube playlist validation and serialization.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class PlaylistBase(BaseModel):
    """Base playlist schema"""

    title: str = Field(..., min_length=1, max_length=500)
    playlist_id: str = Field(..., min_length=1, max_length=100)
    playlist_url: str = Field(..., min_length=1, max_length=500)
    description: Optional[str] = None
    thumbnail_url: Optional[str] = Field(None, max_length=500)
    video_count: Optional[int] = Field(None, ge=0)
    is_featured: bool = False
    display_order: int = 0
    is_visible: bool = True


class PlaylistCreate(PlaylistBase):
    """Schema for creating a new playlist"""

    pass


class PlaylistUpdate(BaseModel):
    """Schema for updating an existing playlist"""

    title: Optional[str] = Field(None, min_length=1, max_length=500)
    description: Optional[str] = None
    thumbnail_url: Optional[str] = Field(None, max_length=500)
    video_count: Optional[int] = Field(None, ge=0)
    is_featured: Optional[bool] = None
    display_order: Optional[int] = None
    is_visible: Optional[bool] = None


class PlaylistSchema(PlaylistBase):
    """Complete playlist schema with database fields"""

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
