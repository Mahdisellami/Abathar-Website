from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Ensemble(Base):
    """Ensemble model for musical groups information"""

    __tablename__ = "ensembles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)  # e.g., "Ogaro Ensemble"
    description = Column(Text, nullable=False)  # Full description of the ensemble
    formation_year = Column(Integer, nullable=True)  # e.g., 2017

    # Musical style and vision
    musical_style = Column(Text, nullable=True)
    vision = Column(Text, nullable=True)

    # Contact information
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(50), nullable=True)

    # Members as JSON array
    # Format: [{"name": "...", "instrument": "...", "origin": "..."}, ...]
    members = Column(JSON, nullable=True)

    # Notable performances/achievements
    highlights = Column(JSON, nullable=True)

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Ensemble(name='{self.name}')>"
