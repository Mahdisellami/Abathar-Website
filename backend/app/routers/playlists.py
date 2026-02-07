"""
Playlists API Router

API endpoints for managing YouTube playlists.
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc

from ..database import get_db
from ..models.playlist import Playlist
from ..schemas.playlist import PlaylistSchema, PlaylistCreate, PlaylistUpdate


router = APIRouter()


@router.get("/playlists", response_model=List[PlaylistSchema])
def get_playlists(
    featured: Optional[bool] = None,
    limit: int = 20,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    """
    Get all visible playlists with optional filtering.

    Args:
        featured: Filter by featured playlists (optional)
        limit: Maximum number of playlists to return (default: 20)
        offset: Number of playlists to skip (default: 0)
        db: Database session

    Returns:
        List of playlists
    """
    query = db.query(Playlist).filter(Playlist.is_visible == True)

    if featured is not None:
        query = query.filter(Playlist.is_featured == featured)

    playlists = (
        query.order_by(Playlist.display_order, desc(Playlist.created_at))
        .offset(offset)
        .limit(limit)
        .all()
    )

    return playlists


@router.get("/playlists/featured", response_model=List[PlaylistSchema])
def get_featured_playlists(
    limit: int = 3,
    db: Session = Depends(get_db),
):
    """
    Get featured playlists for homepage/highlights.

    Args:
        limit: Maximum number of featured playlists to return (default: 3)
        db: Database session

    Returns:
        List of featured playlists
    """
    playlists = (
        db.query(Playlist)
        .filter(Playlist.is_visible == True, Playlist.is_featured == True)
        .order_by(Playlist.display_order, desc(Playlist.created_at))
        .limit(limit)
        .all()
    )

    return playlists


@router.get("/playlists/{playlist_id}", response_model=PlaylistSchema)
def get_playlist(
    playlist_id: int,
    db: Session = Depends(get_db),
):
    """
    Get a single playlist by ID.

    Args:
        playlist_id: Playlist ID
        db: Database session

    Returns:
        Playlist details

    Raises:
        HTTPException: If playlist not found
    """
    playlist = (
        db.query(Playlist)
        .filter(Playlist.id == playlist_id, Playlist.is_visible == True)
        .first()
    )

    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found",
        )

    return playlist


# Admin endpoints (for future admin panel)
@router.post("/admin/playlists", response_model=PlaylistSchema)
def create_playlist(
    playlist: PlaylistCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new playlist (admin only).

    Args:
        playlist: Playlist data
        db: Database session

    Returns:
        Created playlist

    Raises:
        HTTPException: If playlist with same playlist_id already exists
    """
    # Check if playlist with same playlist_id exists
    existing = (
        db.query(Playlist).filter(Playlist.playlist_id == playlist.playlist_id).first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Playlist with this playlist_id already exists",
        )

    db_playlist = Playlist(**playlist.model_dump())
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)

    return db_playlist


@router.put("/admin/playlists/{playlist_id}", response_model=PlaylistSchema)
def update_playlist(
    playlist_id: int,
    playlist: PlaylistUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing playlist (admin only).

    Args:
        playlist_id: Playlist ID
        playlist: Updated playlist data
        db: Database session

    Returns:
        Updated playlist

    Raises:
        HTTPException: If playlist not found
    """
    db_playlist = db.query(Playlist).filter(Playlist.id == playlist_id).first()

    if not db_playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found",
        )

    update_data = playlist.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_playlist, field, value)

    db.commit()
    db.refresh(db_playlist)

    return db_playlist


@router.delete("/admin/playlists/{playlist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_playlist(
    playlist_id: int,
    db: Session = Depends(get_db),
):
    """
    Delete a playlist (admin only).

    Args:
        playlist_id: Playlist ID
        db: Database session

    Raises:
        HTTPException: If playlist not found
    """
    db_playlist = db.query(Playlist).filter(Playlist.id == playlist_id).first()

    if not db_playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found",
        )

    db.delete(db_playlist)
    db.commit()

    return None
