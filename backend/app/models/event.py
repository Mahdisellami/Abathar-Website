from sqlalchemy import Column, Integer, String, Text, Date, Time, Boolean, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Event(Base):
    """Event model for concerts, performances, and workshops"""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    date = Column(Date, nullable=False, index=True)
    time = Column(String(50), nullable=True)  # e.g., "8:00 PM" or "20:00"

    # Location details
    venue = Column(String(255), nullable=False)  # e.g., "Gasteig HP8"
    location = Column(String(255), nullable=True)  # e.g., "Munich, Germany"

    # Event details
    description = Column(Text, nullable=True)
    ensemble_name = Column(String(255), nullable=True)  # e.g., "Ogaro Ensemble"
    event_type = Column(String(100), nullable=True)  # e.g., "concert", "workshop", "children's concert"

    # Status
    is_past = Column(Boolean, default=False, index=True)

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Event(title='{self.title}', date='{self.date}')>"
