"""Unit tests for database models"""
import pytest
from datetime import date
from app.models.event import Event
from app.models.bio import Bio


def test_event_model_with_photo(db_session):
    """Test Event model includes photo_url field"""
    event = Event(
        title="Test Event",
        date=date(2026, 12, 31),
        venue="Test Venue",
        location="Test City",
        photo_url="/images/test.webp",
        is_past=False
    )
    db_session.add(event)
    db_session.commit()

    # Retrieve and verify
    saved_event = db_session.query(Event).first()
    assert saved_event is not None
    assert saved_event.photo_url == "/images/test.webp"
    assert saved_event.title == "Test Event"


def test_event_model_without_photo(db_session):
    """Test Event model works without photo_url (nullable)"""
    event = Event(
        title="Test Event",
        date=date(2026, 12, 31),
        venue="Test Venue",
        location="Test City",
        is_past=False
    )
    db_session.add(event)
    db_session.commit()

    saved_event = db_session.query(Event).first()
    assert saved_event is not None
    assert saved_event.photo_url is None


def test_bio_model(db_session):
    """Test Bio model"""
    bio = Bio(
        name="Test Person",
        title="Test Title",
        bio_text="Test text",
        education=[{"degree": "B.A.", "institution": "Test U", "period": "2020-2024"}],
        achievements=["Test Achievement"],
        current_roles=["Test Role"],
        discography=[]
    )
    db_session.add(bio)
    db_session.commit()

    saved_bio = db_session.query(Bio).first()
    assert saved_bio is not None
    assert saved_bio.name == "Test Person"
    assert len(saved_bio.achievements) == 1
