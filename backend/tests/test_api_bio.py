"""Unit tests for Bio API"""
import pytest


def test_get_bio_empty(client):
    """Test getting bio when database is empty"""
    response = client.get("/api/bio")
    assert response.status_code == 404


def test_get_bio_with_data(client, sample_bio):
    """Test getting bio when data exists"""
    response = client.get("/api/bio")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Musician"
    assert data["title"] == "Test Title"
    assert "education" in data
    assert "achievements" in data


def test_update_bio(client, sample_bio):
    """Test updating bio"""
    update_data = {
        "name": "Updated Musician",
        "title": "Updated Title",
        "bio_text": "Updated bio text",
        "education": [],
        "achievements": ["Test Achievement"],
        "current_roles": [],
        "discography": []
    }
    response = client.put("/api/bio", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Musician"
    assert len(data["achievements"]) == 1
