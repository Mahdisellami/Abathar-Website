# 🐳 Docker Guide - Local Development

This guide shows you how to run the entire Abathar website stack locally using Docker.

## Why Docker?

✅ **No installation needed** - No Python, Node.js, PostgreSQL to install
✅ **One command start** - Everything runs together
✅ **Consistent environment** - Same setup for everyone
✅ **Easy cleanup** - Remove everything with one command
✅ **Dev & Prod modes** - Test both configurations locally

---

## Prerequisites

**Only requirement**: Docker Desktop

- Download: https://www.docker.com/products/docker-desktop
- Install and start Docker Desktop

---

## Quick Start (Easiest)

### Option 1: Using the startup script (Recommended)

```bash
# Development mode (with hot reload)
./start.sh

# Or production mode
./start.sh prod
```

That's it! The script will:
1. Check Docker is running
2. Start all services (database, backend, frontend)
3. Automatically seed the database
4. Show you the URLs

### Option 2: Manual commands

```bash
# Development mode (hot reload)
docker-compose -f docker-compose.dev.yml up -d

# Or production mode
docker-compose up -d

# Seed database (first time only)
docker-compose exec backend python seed_data.py
```

---

## Access Your Application

Once running, visit:

- **Website**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **pgAdmin**: http://localhost:5050 (admin@abathar.com / admin)

---

## Two Modes

### Development Mode (Hot Reload) ⚡

```bash
./start.sh dev
# or
docker-compose -f docker-compose.dev.yml up -d
```

**Features**:
- Code changes auto-reload (no restart needed)
- Frontend: React hot reload
- Backend: Uvicorn auto-reload
- Volume mounting for live code updates

**Use for**: Active development, coding, testing

### Production Mode 🚀

```bash
./start.sh prod
# or
docker-compose up -d
```

**Features**:
- Optimized builds
- Production-ready configuration
- Mimics deployment environment

**Use for**: Testing production build, final QA

---

## Common Commands

### Start Services

```bash
# Development (hot reload)
./start.sh

# Production build
./start.sh prod
```

### Stop Services

```bash
# Stop all
./stop.sh

# Or manually
docker-compose down
docker-compose -f docker-compose.dev.yml down
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend

# Development mode
docker-compose -f docker-compose.dev.yml logs -f
```

### Restart a Service

```bash
# Restart backend
docker-compose restart backend

# Restart frontend
docker-compose restart frontend
```

### Rebuild After Code Changes (Production Mode)

```bash
# Rebuild and restart
docker-compose up -d --build

# Rebuild specific service
docker-compose up -d --build backend
```

### Execute Commands in Containers

```bash
# Open bash in backend
docker-compose exec backend bash

# Run Python script
docker-compose exec backend python seed_data.py

# Open bash in frontend
docker-compose exec frontend sh

# Check database
docker-compose exec postgres psql -U abathar_user -d abathar_website
```

---

## Managing Database

### View Data in pgAdmin

1. Open http://localhost:5050
2. Login: `admin@abathar.com` / `admin`
3. Add Server:
   - Name: Abathar DB
   - Host: `postgres`
   - Port: `5432`
   - Username: `abathar_user`
   - Password: `abathar_password`

### Reset Database

```bash
# Stop services
docker-compose down

# Remove database volume
docker volume rm abathar-website_postgres_data

# Start again (will create fresh database)
./start.sh
```

### Backup Database

```bash
# Backup to file
docker-compose exec postgres pg_dump -U abathar_user abathar_website > backup.sql

# Restore from file
docker-compose exec -T postgres psql -U abathar_user -d abathar_website < backup.sql
```

---

## Development Workflow

### 1. Start Services

```bash
./start.sh
```

### 2. Make Code Changes

Edit files in `backend/` or `frontend/` - changes auto-reload!

**Backend** (`backend/app/`):
- Edit Python files
- Save
- FastAPI reloads automatically

**Frontend** (`frontend/`):
- Edit React components
- Save
- Next.js hot reloads in browser

### 3. View Changes

- Frontend: Refresh http://localhost:3000
- Backend: Check http://localhost:8000/docs

### 4. Check Logs

```bash
# Watch logs
docker-compose -f docker-compose.dev.yml logs -f

# Filter by service
docker-compose -f docker-compose.dev.yml logs -f backend
```

### 5. Stop When Done

```bash
./stop.sh
```

---

## Troubleshooting

### Docker not running

```bash
❌ Error: Docker is not running!
```

**Solution**: Open Docker Desktop

### Port already in use

```bash
Error: port is already allocated
```

**Solution**:
```bash
# Stop existing containers
docker-compose down
docker-compose -f docker-compose.dev.yml down

# Or change ports in docker-compose.yml
```

### Database connection error

**Solution**:
```bash
# Restart database
docker-compose restart postgres

# Wait for health check
docker-compose ps
```

### Frontend can't reach backend

**Solution**: Check `NEXT_PUBLIC_API_URL` is set to `http://localhost:8000` in:
- `docker-compose.yml`
- `docker-compose.dev.yml`

### Need to rebuild

```bash
# Clean rebuild
docker-compose down
docker-compose up -d --build
```

### Remove everything and start fresh

```bash
# Stop and remove containers
docker-compose down

# Remove volumes (deletes database data!)
docker volume rm abathar-website_postgres_data
docker volume rm abathar-website_postgres_data_dev

# Remove images
docker rmi abathar-website-backend
docker rmi abathar-website-frontend

# Start fresh
./start.sh
```

---

## Environment Variables

### Development (.env.docker)

Already configured in `docker-compose.dev.yml`:
- `DATABASE_URL=postgresql://abathar_user:abathar_password@postgres:5432/abathar_website`
- `NEXT_PUBLIC_API_URL=http://localhost:8000`
- `DEBUG=True`

### Production

Same as development but with `DEBUG=False`

---

## Docker Compose Files

### `docker-compose.yml` (Production)
- Builds optimized images
- Production configuration
- No volume mounting

### `docker-compose.dev.yml` (Development)
- Volume mounting for hot reload
- Development configuration
- Faster startup

---

## File Structure

```
/
├── docker-compose.yml           # Production compose
├── docker-compose.dev.yml       # Development compose
├── .env.docker                  # Docker environment vars
├── start.sh                     # Startup script
├── stop.sh                      # Stop script
├── backend/
│   ├── Dockerfile              # Backend image
│   └── .dockerignore
├── frontend/
│   ├── Dockerfile              # Frontend image
│   └── .dockerignore
└── DOCKER_GUIDE.md            # This file
```

---

## Comparison: Docker vs Manual

### Docker (./start.sh)
```
Time: 30 seconds
Steps: 1 command
Requirements: Docker Desktop only
```

### Manual
```
Time: 5+ minutes
Steps: 10+ commands
Requirements: Python, Node.js, PostgreSQL, dependencies
```

---

## Production Deployment vs Local Docker

### Local Docker (Development)
```bash
./start.sh
# Runs on: localhost:3000
# Database: Local PostgreSQL in Docker
# Use for: Development, testing
```

### Production (Deployed)
```bash
# Frontend: Vercel (vercel.com)
# Backend: Render (render.com)
# Database: Supabase (supabase.com)
# Use for: Live website for visitors
```

**Both environments use the same code!**

---

## Quick Reference

```bash
# Start dev
./start.sh

# Start prod
./start.sh prod

# Stop
./stop.sh

# Logs
docker-compose logs -f

# Rebuild
docker-compose up -d --build

# Reset database
docker-compose down
docker volume rm abathar-website_postgres_data
./start.sh

# Clean everything
docker-compose down -v
docker system prune -a
```

---

## Summary

✅ **One command**: `./start.sh`
✅ **Full stack**: Database, Backend, Frontend
✅ **Hot reload**: Code changes apply instantly
✅ **No setup**: Just Docker Desktop

**You now have dev and prod environments!**
- **Dev**: Local Docker (for development)
- **Prod**: Deployed (Vercel + Render + Supabase)

Happy coding! 🚀
