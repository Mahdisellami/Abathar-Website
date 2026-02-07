from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from ..models.video import Video
from ..schemas.video import VideoSchema, VideoCreate, VideoUpdate

router = APIRouter()


@router.get("/videos", response_model=List[VideoSchema])
def get_videos(
    category: Optional[str] = Query(None, description="Filter by category"),
    featured: Optional[bool] = Query(None, description="Filter featured videos"),
    limit: int = Query(20, ge=1, le=100, description="Limit number of results"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    db: Session = Depends(get_db)
):
    """
    Get all visible videos with optional filtering.

    Parameters:
    - category: Filter by category (e.g., 'concert', 'rehearsal', 'interview')
    - featured: True/False to filter featured videos
    - limit: Maximum number of videos to return (default: 20, max: 100)
    - offset: Number of videos to skip for pagination

    Returns videos sorted by display_order, then by published_date (newest first)
    """
    query = db.query(Video).filter(Video.is_visible == True)

    # Apply filters
    if category:
        query = query.filter(Video.category == category)

    if featured is not None:
        query = query.filter(Video.is_featured == featured)

    # Order by display_order (ascending) then by published_date (descending)
    query = query.order_by(Video.display_order.asc(), Video.published_date.desc())

    # Apply pagination
    videos = query.offset(offset).limit(limit).all()
    return videos


@router.get("/videos/featured", response_model=List[VideoSchema])
def get_featured_videos(
    limit: int = Query(3, ge=1, le=20, description="Limit number of featured videos"),
    db: Session = Depends(get_db)
):
    """
    Get featured videos for homepage display.

    Parameters:
    - limit: Maximum number of videos to return (default: 3, max: 20)

    Returns featured videos sorted by display_order
    """
    videos = db.query(Video).filter(
        Video.is_featured == True,
        Video.is_visible == True
    ).order_by(Video.display_order.asc()).limit(limit).all()

    return videos


@router.get("/videos/{video_id}", response_model=VideoSchema)
def get_video(video_id: int, db: Session = Depends(get_db)):
    """
    Get a specific video by ID.
    """
    video = db.query(Video).filter(
        Video.id == video_id,
        Video.is_visible == True
    ).first()

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    return video


@router.get("/videos/by-event/{event_id}", response_model=List[VideoSchema])
def get_videos_by_event(event_id: int, db: Session = Depends(get_db)):
    """
    Get all videos linked to a specific event.

    Parameters:
    - event_id: ID of the event

    Returns videos linked to the event, sorted by display_order
    """
    videos = db.query(Video).filter(
        Video.event_id == event_id,
        Video.is_visible == True
    ).order_by(Video.display_order.asc()).all()

    return videos


@router.post("/videos", response_model=VideoSchema)
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    """
    Create a new video.
    (Future admin feature)

    Checks for duplicate youtube_id to prevent duplicate entries.
    """
    # Check if video with same youtube_id already exists
    existing = db.query(Video).filter(Video.youtube_id == video.youtube_id).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Video with youtube_id '{video.youtube_id}' already exists"
        )

    db_video = Video(**video.model_dump())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


@router.put("/videos/{video_id}", response_model=VideoSchema)
def update_video(
    video_id: int,
    video_update: VideoUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing video.
    (Future admin feature)
    """
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    # If updating youtube_id, check for duplicates
    if video_update.youtube_id and video_update.youtube_id != video.youtube_id:
        existing = db.query(Video).filter(Video.youtube_id == video_update.youtube_id).first()
        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Video with youtube_id '{video_update.youtube_id}' already exists"
            )

    # Update only provided fields
    update_data = video_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(video, field, value)

    db.commit()
    db.refresh(video)
    return video


@router.delete("/videos/{video_id}")
def delete_video(video_id: int, db: Session = Depends(get_db)):
    """
    Delete a video.
    (Future admin feature)
    """
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    db.delete(video)
    db.commit()
    return {"message": "Video deleted successfully"}
