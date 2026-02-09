"""Unit tests for Events API"""
import pytest
from datetime import date


def test_health_check(client):
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_events_empty(client):
    """Test getting events when database is empty"""
    response = client.get("/api/events")
    assert response.status_code == 200
    assert response.json() == []


def test_get_events_with_data(client, sample_event):
    """Test getting events when data exists"""
    response = client.get("/api/events")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Test Concert"
    assert data[0]["venue"] == "Test Venue"
    assert "photo_url" in data[0]  # Critical: photo_url field exists


def test_get_upcoming_events(client, sample_event):
    """Test filtering upcoming events"""
    response = client.get("/api/events?filter_type=upcoming")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["is_past"] is False


def test_create_event(client):
    """Test creating a new event"""
    event_data = {
        "title": "New Concert",
        "date": "2026-06-15",
        "time": "19:00",
        "venue": "New Venue",
        "location": "New City",
        "description": "New Description",
        "ensemble_name": "New Ensemble",
        "event_type": "concert",
        "photo_url": "/images/new.webp",
        "is_past": False
    }
    response = client.post("/api/events", json=event_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Concert"
    assert data["photo_url"] == "/images/new.webp"
    assert "id" in data


def test_create_event_without_photo(client):
    """Test creating event without photo_url (optional field)"""
    event_data = {
        "title": "Concert Without Photo",
        "date": "2026-07-20",
        "venue": "Some Venue",
        "location": "Some City",
        "is_past": False
    }
    response = client.post("/api/events", json=event_data)
    assert response.status_code == 200
    data = response.json()
    assert data["photo_url"] is None


def test_get_single_event(client, sample_event):
    """Test getting a single event by ID"""
    response = client.get(f"/api/events/{sample_event.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == sample_event.id
    assert data["title"] == sample_event.title


def test_get_nonexistent_event(client):
    """Test getting an event that doesn't exist"""
    response = client.get("/api/events/99999")
    assert response.status_code == 404


def test_update_event(client, sample_event):
    """Test updating an event"""
    update_data = {
        "title": "Updated Concert",
        "photo_url": "/images/updated.webp"
    }
    response = client.put(f"/api/events/{sample_event.id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Concert"
    assert data["photo_url"] == "/images/updated.webp"


def test_delete_event(client, sample_event):
    """Test deleting an event"""
    response = client.delete(f"/api/events/{sample_event.id}")
    assert response.status_code == 200

    # Verify it's gone
    response = client.get(f"/api/events/{sample_event.id}")
    assert response.status_code == 404
