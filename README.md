# Abathar Kmash Music Website

Modern full-stack website for Abathar Kmash, a professional oud player, music pedagogue, and composer based in Munich, Germany. This project recreates https://abathar-kmash.de/ with modern technologies and prepares for future AI integrations.

## Live Demo

**Frontend**: https://abathar-website-mj1bdvkyn-bahtas-projects.vercel.app/ (configuring...)
**Backend API**: https://abathar-api.onrender.com
**API Docs**: https://abathar-api.onrender.com/docs

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
- **Media page with video gallery and playlists** 🆕

✅ **YouTube Integration** 🆕
- **24 real performance videos** from Abathar's YouTube channel
- **5 curated playlists** with direct links to YouTube
- Featured videos section on homepage
- Video modal player with autoplay
- Category filtering (concert, performance, interview, rehearsal)
- Playlist cards with gradient backgrounds
- Direct YouTube channel subscription link

✅ **Dual Theme System**
- **Modern Theme**: Clean, minimalist design with warm colors
- **Classic Theme**: Dark theme matching original website
- Toggle button in header, preference saved in localStorage

✅ **Responsive Design**
- Mobile-first approach
- Optimized for all screen sizes
- Smooth animations and transitions

✅ **RESTful API**
- Biography, Events, Ensemble, Videos, and Playlists endpoints
- CRUD operations (admin features prepared)
- Automatic API documentation

✅ **Database Management**
- PostgreSQL with SQLAlchemy ORM
- Automatic seeding on startup
- Structured data for bio, events, ensembles, videos, and playlists
- FORCE_RESEED environment variable for production database updates

## YouTube Integration Details

### Architecture

The YouTube integration stores video and playlist metadata in the database rather than fetching from YouTube API in real-time. This approach provides:

**Benefits:**
- No YouTube API key required
- No rate limits or API quotas
- Full control over displayed content
- Ability to categorize and feature specific videos
- Link videos to specific events
- Custom descriptions and ordering
- Works even if YouTube API is down

**Components:**

1. **Backend Models** (`/backend/app/models/`):
   - `video.py` - Video metadata (title, youtube_id, category, is_featured, etc.)
   - `playlist.py` - Playlist metadata (title, playlist_id, video_count, etc.)

2. **Backend Routers** (`/backend/app/routers/`):
   - `videos.py` - API endpoints for videos (GET /api/videos, /api/videos/featured, etc.)
   - `playlists.py` - API endpoints for playlists (GET /api/playlists, etc.)

3. **Frontend Components** (`/frontend/components/`):
   - `VideoCard.tsx` - Video thumbnail card with play button
   - `VideoGrid.tsx` - Responsive grid layout for videos
   - `VideoModal.tsx` - Modal player with YouTube embed
   - `PlaylistCard.tsx` - Playlist card with gradient background

4. **Frontend Pages**:
   - `/media` - Main videos/playlists page with filtering
   - `/` (homepage) - Featured videos section

### Video Thumbnails

YouTube provides multiple thumbnail sizes for videos:
- `maxresdefault.jpg` (1920x1080) - Only available for high-quality uploads
- `hqdefault.jpg` (480x360) - **Available for ALL videos** ✅ (we use this)
- `mqdefault.jpg` (320x180) - Medium quality fallback
- `default.jpg` (120x90) - Lowest quality

**Important**: Playlists do NOT have direct thumbnail URLs from YouTube. We use gradient backgrounds instead.

### Data Flow

1. **Seeding**: `backend/seed_data.py` populates database with video/playlist metadata
2. **API**: Backend serves video/playlist data via REST endpoints
3. **Frontend**: Fetches data and displays with YouTube embeds
4. **Playback**: Uses YouTube's embed player (no API needed)

### Future Enhancements

- YouTube Data API integration for automatic sync
- View count and engagement metrics
- Automatic thumbnail updates
- Live stream integration
- Comments section

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
- Featured videos section (next 3)
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

### 5. Media (`/media`)
- Video gallery with 24 performance videos
- Category filtering (concert, performance, interview, rehearsal)
- Video modal player with YouTube embed
- Featured videos section
- 5 curated playlists with direct YouTube links
- Playlist cards with gradient backgrounds
- Subscribe to YouTube channel link

### 6. Contact (`/contact`)
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

### Videos
- `GET /api/videos` - Get all videos (supports filtering by category, featured status, limit)
- `GET /api/videos/{id}` - Get single video by ID
- `GET /api/videos/featured` - Get featured videos
- `GET /api/videos/by-event/{event_id}` - Get videos linked to specific event

### Playlists
- `GET /api/playlists` - Get all playlists
- `GET /api/playlists/{id}` - Get single playlist by ID
- `GET /api/playlists/featured` - Get featured playlists

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

### Videos Table
- YouTube ID and URL
- Title, description
- Thumbnail URL, duration
- Published date
- Category (concert, performance, interview, rehearsal)
- Event ID (foreign key to events table)
- Display settings (is_featured, display_order, is_visible)
- Timestamps (created_at, updated_at)

### Playlists Table
- YouTube playlist ID and URL
- Title, description
- Thumbnail URL
- Video count
- Display settings (is_featured, display_order, is_visible)
- Timestamps (created_at, updated_at)

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
FORCE_RESEED=false  # Set to 'true' to clear and reseed database on startup (use once, then remove)
```

**Updating Production Database**:

If you need to update the database with new seed data on Render:

1. Go to your backend service on Render dashboard
2. Navigate to **Environment** tab
3. Add environment variable: `FORCE_RESEED=true`
4. Click **Save Changes**
5. Trigger **Manual Deploy** → **Deploy latest commit**
6. Wait for deployment to complete (check logs for "✓ Cleared X videos and Y playlists")
7. **IMPORTANT**: Remove the `FORCE_RESEED` variable after successful deployment
8. Verify at: `https://abathar-api.onrender.com/api/videos`

This is necessary when:
- Updating placeholder IDs with real YouTube IDs
- Changing video/playlist seed data
- Database has stale data but code is up to date

### Frontend Deployment

**Recommended**: Vercel (optimized for Next.js)

**Setup Steps**:
1. Connect GitHub repo to Vercel
2. In Project Settings → General → Root Directory: Set to `frontend`
3. Add environment variable: `NEXT_PUBLIC_API_URL=https://abathar-api.onrender.com`
4. Deploy

**Important**: Make sure to set the Root Directory to `frontend` in Vercel settings, otherwise you'll get 404 errors.

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

### Adding New Videos

Option 1: Using Seed Script (Recommended)
1. Edit `backend/seed_data.py`
2. Add video data to `videos_data` list:
```python
{
    "title": "Performance Title",
    "youtube_id": "VIDEO_ID_HERE",  # From youtube.com/watch?v=VIDEO_ID_HERE
    "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID_HERE",
    "description": "Performance description",
    "category": "concert",  # concert, performance, interview, rehearsal
    "is_featured": False,
    "display_order": 10,
}
```
3. Clear existing videos (if updating): Connect to database and run `DELETE FROM videos;`
4. Run: `python seed_data.py`
5. Restart backend

Option 2: Using API (Future - when admin panel is ready)
```bash
curl -X POST http://localhost:8000/api/videos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Performance Title",
    "youtube_id": "VIDEO_ID",
    "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID",
    "category": "concert",
    "is_featured": false
  }'
```

### Adding New Playlists

Edit `backend/seed_data.py` and add to `playlists_data` list:
```python
{
    "title": "Playlist Name",
    "playlist_id": "PLAYLIST_ID",  # From youtube.com/playlist?list=PLAYLIST_ID
    "playlist_url": "https://www.youtube.com/playlist?list=PLAYLIST_ID",
    "description": "Playlist description",
    "video_count": 10,
    "is_featured": True,
    "display_order": 1,
}
```

**Note**: YouTube thumbnail URLs use different formats:
- Videos: `https://img.youtube.com/vi/{VIDEO_ID}/hqdefault.jpg` (480x360, always available)
- Playlists: No direct thumbnail URL (we use gradient backgrounds)

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
- Media: /media
- Contact: /contact

# Test video features:
- Click on video cards to open modal player
- Test YouTube embed playback
- Test category filtering
- Verify featured videos on homepage
- Test playlist cards and YouTube links
```

### Full Integration

1. Start PostgreSQL: `docker-compose up -d`
2. Start backend: `cd backend && python app/main.py`
3. Start frontend: `cd frontend && npm run dev`
4. Visit http://localhost:3000
5. Test theme toggle
6. Navigate through all pages (Home, Bio, Events, Ensemble, Media, Contact)
7. Test video playback and playlists on Media page
8. Check API calls in DevTools Network tab
9. Verify no 404 errors in console (thumbnails should load correctly)

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

### Video Thumbnails Not Loading (404 Errors)
- **Local Development**: Database may have placeholder IDs
  - Run: `cd backend && python seed_data.py` to reseed with real YouTube IDs
  - Restart backend
- **Production (Render)**: Database needs reseeding
  - Add environment variable: `FORCE_RESEED=true`
  - Deploy once
  - Remove the environment variable
  - See "Updating Production Database" section above

### Videos/Playlists Not Showing
- Check backend API: `http://localhost:8000/api/videos`
- Check backend API: `http://localhost:8000/api/playlists`
- Verify database has been seeded: `docker exec -it postgres-db psql -U user -d abathar_db -c "SELECT COUNT(*) FROM videos;"`
- Check browser console for API errors

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
