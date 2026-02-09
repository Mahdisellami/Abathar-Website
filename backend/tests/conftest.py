"""Test configuration and fixtures"""
import pytest
from datetime import date
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db
from app.models.event import Event
from app.models.bio import Bio
from app.models.ensemble import Ensemble
from app.models.video import Video
from app.models.playlist import Playlist

# Use in-memory SQLite for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database for each test"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client with database override"""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_event(db_session):
    """Create a sample event for testing"""
    event = Event(
        title="Test Concert",
        date=date(2026, 12, 31),
        time="20:00",
        venue="Test Venue",
        location="Test City",
        description="Test Description",
        ensemble_name="Test Ensemble",
        event_type="concert",
        photo_url="/images/test.webp",
        is_past=False
    )
    db_session.add(event)
    db_session.commit()
    db_session.refresh(event)
    return event


@pytest.fixture
def sample_bio(db_session):
    """Create a sample bio for testing"""
    bio = Bio(
        name="Test Musician",
        title="Test Title",
        bio_text="Test bio text",
        education=[],
        achievements=[],
        current_roles=[],
        discography=[]
    )
    db_session.add(bio)
    db_session.commit()
    db_session.refresh(bio)
    return bio
