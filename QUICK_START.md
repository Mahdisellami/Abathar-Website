# 🚀 Quick Start Guide

Choose your setup method:

---

## Option 1: Docker (Recommended - Easiest) 🐳

### Requirements
- Docker Desktop only

### Start Everything

```bash
# One command - that's it!
./start.sh
```

**Done!** Visit http://localhost:3000

---

## Option 2: Manual Setup

### Requirements
- Python 3.11+
- Node.js 18+
- Docker (for PostgreSQL only)

### Terminal 1: Database

```bash
docker-compose up -d postgres
```

### Terminal 2: Backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
python seed_data.py
python app/main.py
```

### Terminal 3: Frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

---

## What You Get

✅ **Website**: http://localhost:3000
✅ **API**: http://localhost:8000
✅ **API Docs**: http://localhost:8000/docs
✅ **Database UI**: http://localhost:5050

---

## Two Environments

### Development (Local)
```bash
./start.sh          # Local Docker
```

### Production (Deployed)
See `DEPLOYMENT_CHECKLIST.md` for deploying to:
- Vercel (frontend)
- Render (backend)
- Supabase (database)

**Total cost: $0/month** (free tiers)

---

## Need Help?

- **Docker**: See `DOCKER_GUIDE.md`
- **Deployment**: See `DEPLOYMENT_CHECKLIST.md`
- **Full docs**: See `README.md`

---

## Quick Commands

```bash
# Start
./start.sh

# Stop
./stop.sh

# View logs
docker-compose logs -f

# Reset everything
docker-compose down -v
./start.sh
```

---

**You're ready to go!** 🎉
