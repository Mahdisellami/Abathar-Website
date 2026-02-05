# Deployment Checklist

## ☐ Step 1: Database (Supabase)
- [ ] Create Supabase account
- [ ] Create new project
- [ ] Copy connection string
- [ ] Run SQL to create tables
- [ ] Run `deploy_seed.py` to populate data
- [ ] Verify data in Supabase dashboard

**Database URL**: `postgresql://postgres:______@db._____.supabase.co:5432/postgres`

---

## ☐ Step 2: Backend (Render.com)
- [ ] Push code to GitHub
- [ ] Create Render account
- [ ] Create new Web Service
- [ ] Set root directory: `backend`
- [ ] Configure environment variables:
  - [ ] `DATABASE_URL`
  - [ ] `DEBUG=False`
  - [ ] `ALLOWED_ORIGINS`
- [ ] Deploy and wait for completion
- [ ] Test: Visit `https://YOUR-API.onrender.com/docs`

**Backend URL**: `https://________________.onrender.com`

---

## ☐ Step 3: Frontend (Vercel)
- [ ] Update `frontend/.env.production` with backend URL
- [ ] Push to GitHub
- [ ] Create Vercel account
- [ ] Import GitHub repo
- [ ] Set root directory: `frontend`
- [ ] Add environment variable: `NEXT_PUBLIC_API_URL`
- [ ] Deploy and wait for completion
- [ ] Test: Visit your Vercel URL

**Frontend URL**: `https://________________.vercel.app`

---

## ☐ Step 4: Update CORS
- [ ] Go to Render dashboard
- [ ] Update `ALLOWED_ORIGINS` with Vercel URL
- [ ] Save and redeploy

---

## ☐ Step 5: Testing
- [ ] Visit frontend URL
- [ ] Test home page loads
- [ ] Test theme toggle works
- [ ] Navigate to Bio page - check data loads
- [ ] Navigate to Events page - check events display
- [ ] Navigate to Ensemble page - check members show
- [ ] Navigate to Contact page - check info displays
- [ ] Open DevTools → Network tab
- [ ] Verify API calls succeed (200 status)
- [ ] Test on mobile device

---

## ☐ Step 6: Optional Improvements
- [ ] Custom domain (Google Domains ~$12/year)
  - Add to Vercel: Project Settings → Domains
- [ ] Keep Render awake: cron-job.org ping every 14 min
- [ ] Add Google Analytics
- [ ] Set up error monitoring (Sentry free tier)

---

## 🔧 Maintenance

### Update Events
1. Go to Supabase dashboard
2. Table Editor → events
3. Add/edit rows

### Update Bio
1. Go to Supabase dashboard
2. Table Editor → biography
3. Edit the single row

### Redeploy
- Frontend: Push to GitHub (auto-deploys)
- Backend: Push to GitHub (auto-deploys)

---

## 📞 Support Links

- **Supabase Dashboard**: https://supabase.com/dashboard
- **Render Dashboard**: https://dashboard.render.com
- **Vercel Dashboard**: https://vercel.com/dashboard
- **GitHub Repo**: https://github.com/YOUR-USERNAME/abathar-website

---

## 💰 Costs

- Supabase: FREE (500MB)
- Render: FREE (with spin-down)
- Vercel: FREE (unlimited bandwidth)
- **Total: $0/month** ✅

---

## 🚀 Upgrade Path (When Ready)

**For production (no spin-down):**
- Render Starter: $7/month
- Total: $7/month

**With custom domain:**
- Domain: $12/year
- Total: $7/month + $1/month = $8/month

**With AI features:**
- OpenAI API: ~$10-30/month usage
- Total: $17-37/month
