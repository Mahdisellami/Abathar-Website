# Update Render Database with Real Video IDs

The production backend on Render still has placeholder video IDs. Here's how to update it:

## Option 1: Reset Database (Easiest - Recommended)

### Step 1: Access Render Dashboard
1. Go to https://dashboard.render.com/
2. Navigate to your PostgreSQL database service

### Step 2: Delete and Recreate Database
1. In the database dashboard, go to **Settings**
2. Scroll to **Danger Zone**
3. Click **Delete Database**
4. Create a new database with the same name
5. Update the backend service with the new database URL

### Step 3: Restart Backend Service
1. Go to your backend service (abathar-api)
2. Click **Manual Deploy** > **Deploy latest commit**
3. The backend will automatically seed the database with real video IDs on startup

---

## Option 2: Run Update Script on Render

### Step 1: Access Render Shell
1. Go to your backend service on Render
2. Click **Shell** in the top navigation
3. Wait for the shell to connect

### Step 2: Run Update Script
```bash
# Clear existing videos
python -c "from app.database import SessionLocal; from app.models.video import Video; db = SessionLocal(); db.query(Video).delete(); db.commit(); print('Videos cleared')"

# Clear existing playlists
python -c "from app.database import SessionLocal; from app.models.playlist import Playlist; db = SessionLocal(); db.query(Playlist).delete(); db.commit(); print('Playlists cleared')"

# Reseed database
python seed_data.py
```

### Step 3: Restart Service
Click **Manual Deploy** > **Clear build cache & deploy**

---

## Option 3: Use Environment Variable to Force Reseed

### Add to Render Environment Variables:
```
FORCE_RESEED=true
```

Then update `main.py` startup to check this variable and clear data if needed.

---

## Verify Update

After updating, check:
```bash
curl https://abathar-api.onrender.com/api/videos | jq '.[] | {title, youtube_id}' | head -20
```

You should see real YouTube IDs like `epDFxlaZr2E` instead of `PLACEHOLDER_ID_1`.

---

## Current Status

- ✅ Frontend (Vercel): Deployed with latest code
- ❌ Backend (Render): Code deployed but database has old placeholder data
- ✅ Local: Everything working with real IDs

The database just needs to be cleared and reseeded once.
