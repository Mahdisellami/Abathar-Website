"""
Playlist Model

SQLAlchemy model for YouTube playlists.
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Playlist(Base):
    """YouTube Playlist model"""

    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    playlist_id = Column(String(100), unique=True, nullable=False, index=True)  # YouTube playlist ID
    playlist_url = Column(String(500), nullable=False)

    # Metadata
    description = Column(Text, nullable=True)
    thumbnail_url = Column(String(500), nullable=True)
    video_count = Column(Integer, nullable=True)  # Number of videos in playlist

    # Display settings
    is_featured = Column(Boolean, default=False, index=True)
    display_order = Column(Integer, default=0)
    is_visible = Column(Boolean, default=True, index=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Playlist {self.title}>"
