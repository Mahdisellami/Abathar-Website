from sqlalchemy import Column, Integer, String, Text, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Video(Base):
    """Video model for YouTube videos and performances"""

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    youtube_id = Column(String(50), unique=True, nullable=False, index=True)  # e.g., "dQw4w9WgXcQ"
    youtube_url = Column(String(500), nullable=False)

    # Metadata
    description = Column(Text, nullable=True)
    thumbnail_url = Column(String(500), nullable=True)
    duration = Column(String(20), nullable=True)  # e.g., "3:45"
    published_date = Column(Date, nullable=True)

    # Categorization
    category = Column(String(100), nullable=True)  # "concert", "rehearsal", "interview", etc.
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)  # Link to event if applicable

    # Display settings
    is_featured = Column(Boolean, default=False, index=True)
    display_order = Column(Integer, default=0)
    is_visible = Column(Boolean, default=True, index=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship
    event = relationship("Event", backref="videos")

    def __repr__(self):
        return f"<Video(title='{self.title}', youtube_id='{self.youtube_id}')>"
