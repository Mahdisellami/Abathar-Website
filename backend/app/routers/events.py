from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from ..database import get_db
from ..models.event import Event
from ..schemas.event import EventSchema, EventCreate, EventUpdate

router = APIRouter()


@router.get("/events", response_model=List[EventSchema])
def get_events(
    filter_type: Optional[str] = Query(None, description="Filter: 'upcoming', 'past', or 'all'"),
    db: Session = Depends(get_db)
):
    """
    Get all events with optional filtering.

    Parameters:
    - filter_type: 'upcoming' (default), 'past', or 'all'

    Returns events sorted by date (ascending for upcoming, descending for past)
    """
    query = db.query(Event)

    # Apply filter
    if filter_type == "past":
        query = query.filter(Event.is_past == True).order_by(Event.date.desc())
    elif filter_type == "all":
        query = query.order_by(Event.date.asc())
    else:  # 'upcoming' or None (default)
        query = query.filter(Event.is_past == False).order_by(Event.date.asc())

    events = query.all()
    return events


@router.get("/events/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """
    Get a specific event by ID.
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/events", response_model=EventSchema)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    """
    Create a new event.
    (Future admin feature)
    """
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.put("/events/{event_id}", response_model=EventSchema)
def update_event(
    event_id: int,
    event_update: EventUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing event.
    (Future admin feature)
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Update only provided fields
    update_data = event_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(event, field, value)

    db.commit()
    db.refresh(event)
    return event


@router.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    """
    Delete an event.
    (Future admin feature)
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}


@router.post("/events/update-past-status")
def update_past_events_status(db: Session = Depends(get_db)):
    """
    Update is_past status for all events based on current date.
    (Utility endpoint - can be called periodically or via cron)
    """
    today = date.today()

    # Mark past events
    past_count = db.query(Event).filter(
        Event.date < today,
        Event.is_past == False
    ).update({"is_past": True})

    # Mark upcoming events (in case dates were updated)
    upcoming_count = db.query(Event).filter(
        Event.date >= today,
        Event.is_past == True
    ).update({"is_past": False})

    db.commit()

    return {
        "message": "Event statuses updated",
        "marked_as_past": past_count,
        "marked_as_upcoming": upcoming_count
    }
