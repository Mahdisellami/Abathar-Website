from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import create_tables

# Import routers
from .routers import bio, events, ensemble, contact

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
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    create_tables()
    print("Database tables created successfully")


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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
