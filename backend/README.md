# Abathar Kmash Website - Backend

FastAPI backend for the Abathar Kmash music teacher portfolio website.

## Features

- RESTful API with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- Automatic API documentation (Swagger/ReDoc)
- CORS configured for frontend integration
- Prepared structure for future AI features (chatbot, content generation, recommendations)

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (for PostgreSQL)
- pip or poetry for package management

## Quick Start

### 1. Start Database

```bash
# From project root
docker-compose up -d
```

This starts:
- PostgreSQL on port 5432
- pgAdmin on port 5050 (http://localhost:5050)

pgAdmin credentials:
- Email: admin@abathar.com
- Password: admin

### 2. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env if needed (default values work for local development)
```

### 4. Run the API Server

```bash
# From backend directory
python -m uvicorn app.main:app --reload

# Or use the shortcut
python app/main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry
│   ├── config.py            # Settings and configuration
│   ├── database.py          # Database connection
│   ├── models/              # SQLAlchemy ORM models
│   │   ├── bio.py
│   │   ├── event.py
│   │   └── ensemble.py
│   ├── schemas/             # Pydantic validation schemas
│   │   ├── bio.py
│   │   ├── event.py
│   │   └── ensemble.py
│   ├── routers/             # API route handlers
│   │   ├── bio.py
│   │   ├── events.py
│   │   ├── ensemble.py
│   │   └── contact.py
│   └── ai/                  # Future AI features
│       ├── chatbot.py
│       ├── content_gen.py
│       └── recommendations.py
├── alembic/                 # Database migrations
├── requirements.txt
├── .env.example
└── README.md
```

## API Endpoints

### Biography
- `GET /api/bio` - Get biography information
- `PUT /api/bio` - Update biography (future admin)

### Events
- `GET /api/events` - Get all events (filter: upcoming/past)
- `GET /api/events/{id}` - Get specific event
- `POST /api/events` - Create event (future admin)
- `PUT /api/events/{id}` - Update event (future admin)
- `DELETE /api/events/{id}` - Delete event (future admin)

### Ensemble
- `GET /api/ensemble` - Get ensemble information
- `PUT /api/ensemble` - Update ensemble (future admin)

### Contact
- `POST /api/contact` - Send contact message (future feature)

## Database Management

### Access PostgreSQL directly

```bash
docker exec -it abathar_db psql -U abathar_user -d abathar_website
```

### Use pgAdmin

1. Open http://localhost:5050
2. Login with admin@abathar.com / admin
3. Add server:
   - Name: Abathar DB
   - Host: postgres
   - Port: 5432
   - Username: abathar_user
   - Password: abathar_password

### Reset Database

```bash
# Stop containers
docker-compose down -v

# Restart
docker-compose up -d
```

## Future AI Features

The `/app/ai/` directory contains placeholder modules for future AI integrations:

### Chatbot (`chatbot.py`)
- Visitor assistance
- Answer questions about lessons, availability, music
- Integration: OpenAI GPT-4 or Anthropic Claude

### Content Generation (`content_gen.py`)
- Auto-generate event descriptions
- Create social media posts
- Update bio sections
- Integration: LLM APIs with custom prompts

### Music Recommendations (`recommendations.py`)
- Suggest similar artists
- Recommend events based on interests
- Integration: Embedding models + vector search (pgvector)

### To implement AI features:

1. Add API keys to `.env`:
```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

2. Install additional dependencies:
```bash
pip install openai anthropic langchain
```

3. Implement functions in the AI modules
4. Add corresponding API endpoints in routers

## Development

### Run with auto-reload

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run tests (when implemented)

```bash
pytest
```

### Code formatting

```bash
black app/
isort app/
```

## Production Deployment

### Recommended Hosting
- Railway.app (easy PostgreSQL + app hosting)
- Render.com
- DigitalOcean App Platform
- AWS ECS/Fargate

### Environment Variables
Set these in production:
- `DATABASE_URL` - Production PostgreSQL connection string
- `DEBUG=False` - Disable debug mode
- `ALLOWED_ORIGINS` - Frontend production URL
- AI API keys (when implementing AI features)

### Run in production mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Troubleshooting

### Database connection errors
- Ensure Docker is running: `docker ps`
- Check database is healthy: `docker-compose ps`
- Verify connection string in `.env`

### Import errors
- Ensure you're in the backend directory
- Check all __init__.py files exist
- Reinstall dependencies: `pip install -r requirements.txt`

### CORS errors
- Update `ALLOWED_ORIGINS` in `.env` with frontend URL
- Restart API server after changes

## Support

For issues or questions, contact: abathar.k987@gmail.com
