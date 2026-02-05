# Abathar Kmash Music Website

Modern full-stack website for Abathar Kmash, a professional oud player, music pedagogue, and composer based in Munich, Germany. This project recreates https://abathar-kmash.de/ with modern technologies and prepares for future AI integrations.

## Overview

**Backend**: FastAPI + PostgreSQL
**Frontend**: Next.js 14 + TypeScript + Tailwind CSS
**Features**: Dual theme system (Modern & Classic), prepared for AI chatbot, content generation, and music recommendations

## Project Structure

```
/
├── backend/              # FastAPI Backend
│   ├── app/
│   │   ├── main.py      # FastAPI app entry
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── routers/     # API endpoints
│   │   └── ai/          # AI features (placeholders)
│   ├── seed_data.py     # Database seeding script
│   └── requirements.txt
│
├── frontend/             # Next.js Frontend
│   ├── app/             # Pages (App Router)
│   ├── components/      # React components
│   ├── lib/             # API client & utilities
│   └── styles/          # Tailwind CSS
│
├── docker-compose.yml   # PostgreSQL setup
└── README.md           # This file
```

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose

### 1. Start Database

```bash
docker-compose up -d
```

This starts PostgreSQL on port 5432 and pgAdmin on port 5050.

### 2. Setup Backend

```bash
# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Seed database with initial data
python seed_data.py

# Start FastAPI server
python app/main.py
```

Backend will be available at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs

### 3. Setup Frontend

```bash
# Navigate to frontend (in a new terminal)
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.local.example .env.local

# Start development server
npm run dev
```

Frontend will be available at: http://localhost:3000

## Features

### Current Features

✅ **Complete Portfolio Website**
- Home page with hero section and featured events
- Biography page with education and achievements
- Events page with upcoming/past filtering
- Ogaro Ensemble page with member profiles
- Contact page with Impressum

✅ **Dual Theme System**
- **Modern Theme**: Clean, minimalist design with warm colors
- **Classic Theme**: Dark theme matching original website
- Toggle button in header, preference saved in localStorage

✅ **Responsive Design**
- Mobile-first approach
- Optimized for all screen sizes
- Smooth animations and transitions

✅ **RESTful API**
- Biography, Events, and Ensemble endpoints
- CRUD operations (admin features prepared)
- Automatic API documentation

✅ **Database Management**
- PostgreSQL with SQLAlchemy ORM
- Seeded with content from original website
- Structured data for bio, events, and ensembles

### Future Features (Prepared)

🚀 **AI Chatbot**
- Answer visitor questions about lessons, availability, events
- Integration points: OpenAI GPT-4 or Anthropic Claude
- See: `backend/app/ai/chatbot.py`

🚀 **Content Generation**
- Auto-generate event descriptions
- Create social media posts
- Generate bio summaries
- See: `backend/app/ai/content_gen.py`

🚀 **Music Recommendations**
- Suggest similar artists
- Recommend events based on interests
- Vector embeddings support (pgvector ready)
- See: `backend/app/ai/recommendations.py`

## Pages

### 1. Home (`/`)
- Hero section with call-to-action
- Introduction
- Featured upcoming events (next 3)
- Music lessons CTA

### 2. Biography (`/bio`)
- Complete bio with personal background
- Education timeline
- Current professional roles
- Notable achievements
- Discography

### 3. Events (`/events`)
- Filter: Upcoming, Past, or All
- Event cards with date, venue, location
- Ensemble and event type tags

### 4. Ensemble (`/ensemble`)
- Ogaro Ensemble description
- Musical style and vision
- Member profiles with instruments
- Performance highlights
- Booking information

### 5. Contact (`/contact`)
- Contact details (email, phone, address)
- Ogaro Ensemble contact
- Impressum (legal information)
- Contact form (placeholder for future)

## API Endpoints

### Biography
- `GET /api/bio` - Get biography
- `PUT /api/bio` - Update biography

### Events
- `GET /api/events?filter_type=upcoming` - Get events
- `GET /api/events/{id}` - Get single event
- `POST /api/events` - Create event
- `PUT /api/events/{id}` - Update event
- `DELETE /api/events/{id}` - Delete event
- `POST /api/events/update-past-status` - Update past/upcoming status

### Ensemble
- `GET /api/ensemble` - Get main ensemble
- `GET /api/ensembles` - Get all ensembles
- `GET /api/ensembles/{id}` - Get ensemble by ID
- `POST /api/ensembles` - Create ensemble
- `PUT /api/ensemble` - Update main ensemble

### Contact
- `GET /api/contact-info` - Get contact details
- `POST /api/contact` - Send message (placeholder)

## Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM for database
- **PostgreSQL**: Relational database
- **Pydantic**: Data validation
- **Alembic**: Database migrations (ready)

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type safety
- **Tailwind CSS**: Utility-first CSS
- **Axios**: HTTP client
- **date-fns**: Date formatting

### DevOps
- **Docker**: PostgreSQL containerization
- **pgAdmin**: Database management UI

## Database Schema

### Bio Table
- Personal information and title
- Education (JSON)
- Achievements (JSON)
- Current roles (JSON)
- Discography (JSON)

### Events Table
- Title, date, time, venue, location
- Description, ensemble name, event type
- is_past flag for filtering

### Ensembles Table
- Name, description, formation year
- Musical style and vision
- Contact info (email, phone)
- Members (JSON)
- Highlights (JSON)

## Theme System

Users can toggle between two themes:

**Modern Theme**:
- Light background
- Warm color palette (gold, teal, burgundy)
- Modern typography
- Clean, professional design

**Classic Theme**:
- Dark background (#1a1a1a)
- Gold accents (#d4af37)
- Resembles original WordPress site
- Traditional, elegant design

Toggle button in header (sun/moon icon). Preference persists via localStorage.

## Deployment

### Backend Deployment

**Recommended Platforms**:
- Railway.app
- Render.com
- DigitalOcean App Platform

**Environment Variables**:
```env
DATABASE_URL=postgresql://...
DEBUG=False
ALLOWED_ORIGINS=https://your-frontend-url.com
```

### Frontend Deployment

**Recommended**: Vercel (optimized for Next.js)

**Environment Variables**:
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

**Alternative Platforms**:
- Netlify
- Cloudflare Pages
- AWS Amplify

### Database

**Recommended**:
- Railway PostgreSQL
- Supabase
- DigitalOcean Managed Database

## Development Workflow

### Adding New Events

Option 1: Using pgAdmin
1. Open http://localhost:5050
2. Connect to database
3. Insert into events table

Option 2: Using API
```bash
curl -X POST http://localhost:8000/api/events \
  -H "Content-Type: application/json" \
  -d '{"title": "Concert", "date": "2026-12-31", ...}'
```

Option 3: Database seeding
- Edit `backend/seed_data.py`
- Run `python seed_data.py`

### Implementing AI Features

1. Add API keys to `backend/.env`:
```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

2. Install AI libraries:
```bash
pip install openai anthropic langchain
```

3. Implement functions in `backend/app/ai/`:
- `chatbot.py` - Chat functionality
- `content_gen.py` - Content generation
- `recommendations.py` - Recommendations

4. Add API endpoints in new router
5. Connect frontend components

## Content Management

Currently, content is managed through:
1. Direct database edits (pgAdmin)
2. API endpoints (using Swagger UI)
3. Seed script updates

**Future**: Admin panel with authentication

## Testing

### Backend

```bash
# Start backend
cd backend
python app/main.py

# Open browser
http://localhost:8000/docs

# Test endpoints via Swagger UI
```

### Frontend

```bash
# Start frontend
cd frontend
npm run dev

# Open browser
http://localhost:3000

# Test all pages:
- Home: /
- Bio: /bio
- Events: /events
- Ensemble: /ensemble
- Contact: /contact
```

### Full Integration

1. Start PostgreSQL: `docker-compose up -d`
2. Start backend: `cd backend && python app/main.py`
3. Start frontend: `cd frontend && npm run dev`
4. Visit http://localhost:3000
5. Test theme toggle
6. Navigate through all pages
7. Check API calls in DevTools Network tab

## Troubleshooting

### Database Connection Failed
```bash
# Check Docker is running
docker ps

# Restart containers
docker-compose down
docker-compose up -d
```

### CORS Errors
- Check `ALLOWED_ORIGINS` in `backend/.env`
- Restart backend after changes

### Frontend Can't Reach Backend
- Verify backend is running: `http://localhost:8000/health`
- Check `NEXT_PUBLIC_API_URL` in `frontend/.env.local`

### Theme Not Working
- Clear browser localStorage
- Hard refresh (Cmd+Shift+R or Ctrl+Shift+F5)

## Contributing

This is a personal portfolio project. For suggestions or issues, contact abathar.k987@gmail.com.

## Credits

- **Original Website**: https://abathar-kmash.de/
- **WordPress Theme**: Euphony by Catch Themes
- **Photos**: Marie Lehmann (@mariellemilia)
- **Built with**: FastAPI, Next.js, PostgreSQL

## License

See LICENSE file.

## Contact

**Abathar Kmash**
- Email: abathar.k987@gmail.com
- Phone: +49 176 20360789
- Ogaro Ensemble: ogaro.ensemble@gmail.com

---

Built with ❤️ for transcultural music and education
