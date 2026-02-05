from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Bio(Base):
    """Biography model for storing musician's professional information"""

    __tablename__ = "biography"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    title = Column(String(500), nullable=False)  # e.g., "Oud Player | Music Pedagogue | Composer"
    bio_text = Column(Text, nullable=False)  # Main biography text

    # JSON fields for structured data
    education = Column(JSON, nullable=True)  # List of education entries
    achievements = Column(JSON, nullable=True)  # List of achievements
    current_roles = Column(JSON, nullable=True)  # List of current professional roles
    discography = Column(JSON, nullable=True)  # List of recordings/albums

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Bio(name='{self.name}')>"
