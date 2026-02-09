# Testing & Deployment Guide

## 🚨 CRITICAL: Test Before Pushing to Production

**NEVER push database schema changes without local testing first!**

## Local Testing Workflow with Docker

### Prerequisites
- Docker & Docker Compose installed
- Terminal access

### Step 1: Start Local Environment

```bash
# From project root
docker-compose up -d
```

This starts:
- PostgreSQL on `localhost:5432`
- pgAdmin on `localhost:5050`

### Step 2: Test Backend Locally

```bash
cd backend

# Set environment to use local database
export DATABASE_URL="postgresql://user:password@localhost:5432/abathar_db"
export DEBUG=True
export FORCE_RESEED=true  # If testing schema changes

# Install dependencies (if not done)
pip install -r requirements.txt

# Run backend
python app/main.py
```

**Expected Output:**
```
Database tables created successfully
Seeding bio...
Seeding events...
Seeded X events successfully!
...
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 3: Test API Endpoints

Open browser or use curl:

```bash
# Health check
curl http://localhost:8000/health

# Test events endpoint (the one that was broken!)
curl http://localhost:8000/api/events?filter_type=upcoming

# Test bio
curl http://localhost:8000/api/bio

# Test videos
curl http://localhost:8000/api/videos/featured?limit=3
```

**All endpoints should return 200 OK with JSON data.**

### Step 4: Test Frontend Locally

```bash
cd frontend

# Make sure it points to local backend
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Install dependencies (if not done)
npm install

# Run development server
npm run dev
```

Open http://localhost:3000 and test:
- ✅ Homepage loads
- ✅ Events page loads
- ✅ Bio page loads
- ✅ Media page loads
- ✅ Gallery page loads
- ✅ No console errors

### Step 5: Test Production Build

```bash
# Still in frontend directory
npm run build

# Should complete without errors
# Check for:
# ✓ Compiled successfully
# ✓ Linting and checking validity of types
# ✓ Generating static pages (X/X)
```

### Step 6: Clean Up After Testing

```bash
# Stop Docker containers
docker-compose down

# Remove test environment variable
unset FORCE_RESEED
```

---

## Pre-Deployment Checklist

**Before pushing ANY code that touches the database:**

- [ ] Backend runs locally without errors
- [ ] All API endpoints return 200 OK
- [ ] Frontend builds successfully (`npm run build`)
- [ ] Frontend connects to local backend
- [ ] All pages load without console errors
- [ ] Database seeding completes successfully
- [ ] Schema changes are properly handled (migrations or FORCE_RESEED)
- [ ] Environment variables documented
- [ ] README updated if needed

**If ANY checkbox is unchecked, DO NOT PUSH!**

---

## Database Schema Changes Process

### When Adding/Modifying Database Fields:

1. **Update Model** (e.g., `backend/app/models/event.py`)
   ```python
   photo_url = Column(String(500), nullable=True)
   ```

2. **Update Schema** (e.g., `backend/app/schemas/event.py`)
   ```python
   photo_url: Optional[str] = Field(None, max_length=500)
   ```

3. **Update TypeScript Types** (e.g., `frontend/lib/types.ts`)
   ```typescript
   photo_url?: string;
   ```

4. **Update Seed Data** (e.g., `backend/seed_data.py`)
   ```python
   Event(
       title="...",
       photo_url="/images/performances/performance-01.webp",
       ...
   )
   ```

5. **Test Locally with FORCE_RESEED=true**
   - Verify old data is cleared
   - Verify new schema is created
   - Verify seeding works

6. **Update FORCE_RESEED Logic** (if needed)
   - Make sure all affected tables are cleared
   - Check `backend/app/main.py` startup event

7. **Only After All Tests Pass:**
   - Commit changes
   - Push to GitHub
   - Update Render environment variables
   - Monitor deployment logs

---

## Common Issues & Solutions

### Issue: "Column does not exist" Error

**Cause:** Database has old schema, code expects new schema

**Solution:**
1. Set `FORCE_RESEED=true` in Render environment
2. Redeploy
3. Check logs for successful clear + reseed
4. Remove `FORCE_RESEED`

### Issue: CORS Errors in Production

**Cause:** Frontend URL not in `ALLOWED_ORIGINS`

**Solution:**
1. Update `ALLOWED_ORIGINS` in Render environment
2. Include all Vercel URLs (production + preview)
3. Redeploy

### Issue: 500 Internal Server Error

**Cause:** Usually database schema mismatch or missing data

**Solution:**
1. Check Render logs for Python stack trace
2. Identify which model/table is causing issues
3. Test locally with same data
4. Apply fix and test before pushing

---

## Production Deployment Workflow

### Standard Code Changes (No Schema Changes)

```bash
# 1. Test locally
npm run build  # frontend
python app/main.py  # backend

# 2. Commit and push
git add .
git commit -m "Your message"
git push origin main

# 3. Verify on Render
# - Watch deployment logs
# - Test live site
# - Check for errors
```

### Database Schema Changes (CRITICAL)

```bash
# 1. Test EXTENSIVELY locally with Docker
docker-compose up -d
export FORCE_RESEED=true
python app/main.py  # Verify seeding works
npm run build  # Verify frontend builds

# 2. Update documentation
# - Document new fields in README
# - Update API docs if needed

# 3. Commit and push
git add .
git commit -m "Add [field] to [model] - REQUIRES FORCE_RESEED"
git push origin main

# 4. Update Render environment BEFORE deployment
# - Add FORCE_RESEED=true
# - Verify ALLOWED_ORIGINS is correct

# 5. Deploy and monitor
# - Watch logs carefully
# - Look for successful clear + reseed messages
# - Test all endpoints

# 6. Clean up
# - Remove FORCE_RESEED
# - Test site again
```

---

## Emergency Rollback

If deployment breaks production:

1. **Quick Fix:** Revert to last working commit
   ```bash
   git revert HEAD
   git push origin main
   ```

2. **Database Restore:** If database is corrupted
   - Contact Render support
   - Or: Set FORCE_RESEED=true to rebuild from seed data

3. **Temporary Fix:** Point frontend to old backend version
   - Update Vercel environment variable temporarily
   - Buy time to fix properly

---

## Testing Checklist Template

Copy this for each deployment:

```
## Pre-Deployment Test Results

Date: ___________
Branch: __________
Changes: _________

### Backend Tests
- [ ] Docker PostgreSQL running
- [ ] Backend starts without errors
- [ ] /health returns 200
- [ ] /api/bio returns 200
- [ ] /api/events returns 200
- [ ] /api/videos returns 200
- [ ] Database seeding successful
- [ ] No Python errors in console

### Frontend Tests
- [ ] npm run build succeeds
- [ ] npm run dev works
- [ ] Homepage loads (localhost:3000)
- [ ] Bio page loads
- [ ] Events page loads
- [ ] Media page loads
- [ ] Gallery page loads
- [ ] No console errors
- [ ] API calls succeed

### Schema Changes (if applicable)
- [ ] Model updated
- [ ] Schema updated
- [ ] TypeScript types updated
- [ ] Seed data updated
- [ ] FORCE_RESEED tested locally
- [ ] All tables cleared correctly

### Deployment
- [ ] Code pushed to GitHub
- [ ] Environment variables updated on Render
- [ ] Deployment logs monitored
- [ ] Live site tested
- [ ] FORCE_RESEED removed (if used)
- [ ] Final verification complete

**Status:** ✅ PASS / ❌ FAIL

**Notes:**
```

---

## Lessons Learned

### What Went Wrong (This Incident)

1. ❌ Added `photo_url` to Event model
2. ❌ Pushed to production without local testing
3. ❌ FORCE_RESEED only cleared Videos/Playlists, not Events
4. ❌ Production database had old schema
5. ❌ /api/events returned 500 errors
6. ❌ Frontend broke for users

### What Should Have Happened

1. ✅ Update Event model locally
2. ✅ Test with Docker + FORCE_RESEED
3. ✅ Verify ALL endpoints work
4. ✅ Update FORCE_RESEED to clear Events
5. ✅ Test again
6. ✅ Frontend build test
7. ✅ THEN push to production

### Key Takeaway

**"If it's not tested locally, it doesn't work in production."**

---

## Monitoring Production

### Health Check URLs

- Backend: https://abathar-api.onrender.com/health
- Backend Docs: https://abathar-api.onrender.com/docs
- Frontend: https://abathar-website.vercel.app

### Quick Production Test

```bash
# Test all critical endpoints
curl https://abathar-api.onrender.com/health
curl https://abathar-api.onrender.com/api/events?filter_type=upcoming
curl https://abathar-api.onrender.com/api/bio
curl https://abathar-api.onrender.com/api/videos/featured?limit=3
```

All should return 200 OK.

### Render Logs

Always check after deployment:
1. Go to Render dashboard
2. Click your service
3. Click "Logs" tab
4. Look for errors or warnings

### Vercel Logs

For frontend issues:
1. Go to Vercel dashboard
2. Click your project
3. Click "Deployments"
4. Click latest deployment
5. Check "Functions" and "Build Logs"

---

**Remember: Production is sacred. Test everything locally first!** 🚀
