from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import create_tables
import sys
import os

# Add parent directory to path to import seed_data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seed_data import seed_database

# Import routers
from .routers import bio, events, ensemble, contact, videos, playlists

app = FastAPI(
    title="Abathar Kmash Music Website API",
    description="API for musician portfolio website with AI features support",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    import os
    from .models.video import Video
    from .models.playlist import Playlist
    from .models.event import Event
    from .models.bio import Bio
    from .models.ensemble import Ensemble
    from .database import SessionLocal

    create_tables()
    print("Database tables created successfully")

    # Check if FORCE_RESEED environment variable is set
    if os.getenv("FORCE_RESEED", "false").lower() == "true":
        print("🔄 FORCE_RESEED detected - clearing ALL existing data...")
        db = SessionLocal()
        try:
            video_count = db.query(Video).delete()
            playlist_count = db.query(Playlist).delete()
            event_count = db.query(Event).delete()
            bio_count = db.query(Bio).delete()
            ensemble_count = db.query(Ensemble).delete()
            db.commit()
            print(f"✓ Cleared {video_count} videos, {playlist_count} playlists, {event_count} events, {bio_count} bios, {ensemble_count} ensembles")
        except Exception as e:
            print(f"Warning: Error clearing data: {e}")
            db.rollback()
        finally:
            db.close()

    # Seed database with initial data (safe to run multiple times)
    try:
        seed_database()
    except Exception as e:
        print(f"Warning: Database seeding encountered an error: {e}")
        print("Continuing with startup...")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Abathar Kmash Music Website API",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check for monitoring"""
    return {"status": "healthy"}


# Include routers
app.include_router(bio.router, prefix="/api", tags=["Biography"])
app.include_router(events.router, prefix="/api", tags=["Events"])
app.include_router(ensemble.router, prefix="/api", tags=["Ensemble"])
app.include_router(contact.router, prefix="/api", tags=["Contact"])
app.include_router(videos.router, prefix="/api", tags=["Videos"])
app.include_router(playlists.router, prefix="/api", tags=["Playlists"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
