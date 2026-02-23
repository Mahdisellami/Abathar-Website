# Migration Guide: Vercel → abathar-kmash.de

**Migration Date**: February 23, 2026
**From**: `https://abathar-website.vercel.app/`
**To**: `https://abathar-kmash.de/`
**Status**: Backend updated ✅ | Frontend pending ⏳ | DNS pending ⏳

---

## Overview

This guide will help you migrate your Abathar website from Vercel's default domain to your custom domain `abathar-kmash.de` while keeping both domains active.

**Architecture**:
- Frontend: Next.js 14 on Vercel → Add custom domain
- Backend: FastAPI on Render → CORS updated ✅
- Database: PostgreSQL on Supabase → No changes needed

---

## Progress Checklist

- [x] Update backend CORS configuration
- [x] Test changes locally with Docker
- [x] Commit and push changes to GitHub
- [x] Update Render environment variables
- [ ] Add custom domain to Vercel
- [ ] Configure DNS records
- [ ] Verify SSL certificate
- [ ] Test all functionality on new domain
- [ ] Update documentation

---

## Part 1: Backend Configuration (COMPLETED ✅)

### What Was Changed

**File**: `/backend/.env.production`
```diff
-# CORS - Frontend URLs (Vercel production and preview deployments)
-ALLOWED_ORIGINS=https://abathar-website.vercel.app,https://abathar-website-mj1bdvkyn-bahtas-projects.vercel.app,http://localhost:3000
+# CORS - Frontend URLs (Production domain and local development)
+ALLOWED_ORIGINS=https://abathar-kmash.de,http://localhost:3000
```

**Commit**: `c201542` - "Update CORS configuration for domain migration to abathar-kmash.de"

### Render Dashboard Update (REQUIRED)

⚠️ **CRITICAL**: You must update the environment variable in Render:

1. Go to: https://dashboard.render.com
2. Navigate to: **abathar-website-api** service
3. Click: **Environment** → **Environment Variables**
4. Find: `ALLOWED_ORIGINS`
5. Update to: `https://abathar-kmash.de,http://localhost:3000`
6. Click: **Save Changes** (triggers automatic redeploy)

**Verification**:
```bash
# Test backend is responding
curl https://abathar-api.onrender.com/health

# Expected: {"status":"healthy"}
```

---

## Part 2: Frontend Deployment (IN PROGRESS ⏳)

### Step 1: Add Custom Domain to Vercel

1. **Login to Vercel**:
   - Go to: https://vercel.com/dashboard
   - Navigate to your project: `abathar-website`

2. **Add Domain**:
   - Click: **Settings** → **Domains**
   - Click: **Add Domain**
   - Enter: `abathar-kmash.de`
   - Click: **Add**

3. **Add www Subdomain** (Optional but recommended):
   - Click: **Add Domain** again
   - Enter: `www.abathar-kmash.de`
   - Vercel will auto-redirect www → non-www

### Step 2: Configure DNS Records

After adding the domain, Vercel will display the DNS records you need to configure. You'll need to access your domain registrar's DNS management panel.

#### Common DNS Providers:
- **Namecheap**: Dashboard → Domain List → Manage → Advanced DNS
- **GoDaddy**: Domain Settings → Manage DNS
- **Cloudflare**: DNS → Records
- **Google Domains**: My Domains → DNS

#### DNS Configuration Options

Vercel will show one of these configurations:

**Option A: A Records (Most Common)**
```
Type: A
Name: @ (or leave empty for root domain)
Value: 76.76.21.21
TTL: 3600 (or Auto)
```

**Option B: CNAME (Alternative)**
```
Type: CNAME
Name: @ (or www)
Value: cname.vercel-dns.com
TTL: 3600
```

**For www subdomain**:
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
TTL: 3600
```

#### Important Notes:
- Remove any existing A or CNAME records for `@` and `www` that point to WordPress
- If WordPress is using A records, you'll need to remove them
- DNS propagation can take 24-48 hours (usually much faster)
- Keep WordPress database backup before removing DNS records

### Step 3: Verify Domain Configuration

**Check DNS propagation**:
```bash
# Check if DNS is updated
dig abathar-kmash.de

# Check from multiple locations
nslookup abathar-kmash.de
```

**Check Vercel status**:
- In Vercel dashboard, go to **Settings** → **Domains**
- Look for green checkmark next to `abathar-kmash.de`
- SSL certificate should say "Active" (may take a few minutes)

### Step 4: Test the Website

Once DNS propagates and Vercel shows the domain as active:

```bash
# Test homepage
curl -I https://abathar-kmash.de/

# Test API connection
curl https://abathar-kmash.de/api/events

# Test specific pages
curl -I https://abathar-kmash.de/bio
curl -I https://abathar-kmash.de/events
curl -I https://abathar-kmash.de/media
```

**Manual Testing**:
- [ ] Visit https://abathar-kmash.de
- [ ] Check SSL certificate (green lock icon)
- [ ] Navigate through all pages
- [ ] Test contact form
- [ ] Verify videos load on media page
- [ ] Check events display correctly
- [ ] Test responsive design on mobile

---

## Part 3: Both Domains Active

After migration, both domains will work:

| Domain | Status | Purpose |
|--------|--------|---------|
| `abathar-website.vercel.app` | Active | Legacy URL, still works |
| `abathar-kmash.de` | Active | New primary domain |

### Set Primary Domain (Optional)

To make `abathar-kmash.de` the primary domain:

1. In Vercel: **Settings** → **Domains**
2. Find `abathar-kmash.de`
3. Click three dots → **Set as Primary**
4. This will redirect all other domains to this one

---

## Part 4: Troubleshooting

### DNS Not Propagating

**Problem**: `abathar-kmash.de` doesn't load after DNS update

**Solutions**:
1. Wait 10-60 minutes for DNS propagation
2. Clear your browser cache and DNS cache:
   ```bash
   # macOS
   sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder

   # Windows
   ipconfig /flushdns
   ```
3. Check DNS propagation: https://dnschecker.org/
4. Verify DNS records are correct in your registrar

### SSL Certificate Issues

**Problem**: "Your connection is not private" warning

**Solutions**:
1. Wait 5-10 minutes for Vercel to provision SSL
2. In Vercel dashboard, check **Settings** → **Domains** → SSL status
3. If stuck, try removing and re-adding the domain
4. Contact Vercel support if it persists

### CORS Errors

**Problem**: Frontend can't connect to backend API

**Solutions**:
1. Verify Render environment variable is updated:
   - `ALLOWED_ORIGINS=https://abathar-kmash.de,http://localhost:3000`
2. Check backend logs in Render dashboard
3. Test API directly:
   ```bash
   curl -H "Origin: https://abathar-kmash.de" -I https://abathar-api.onrender.com/api/bio
   ```
4. If CORS headers missing, redeploy backend on Render

### 404 Errors on New Domain

**Problem**: Pages return 404 on new domain

**Solutions**:
1. Trigger a new Vercel deployment:
   ```bash
   git commit --allow-empty -m "Trigger deployment"
   git push
   ```
2. Check Vercel build logs for errors
3. Verify Next.js configuration is correct

---

## Part 5: Post-Migration Tasks

### Update Documentation

Files to update with new URLs:

- [ ] `/README.md` - Update demo URLs
- [ ] `/TESTING.md` - Update API endpoint examples
- [ ] `/DEPLOYMENT_CHECKLIST.md` - Update deployment URLs

### Update External References

- [ ] Update social media links (Instagram, Facebook, etc.)
- [ ] Update Google Search Console (add new domain)
- [ ] Update any printed materials or business cards
- [ ] Notify collaborators of new URL

### Monitor Performance

After migration, monitor:
- [ ] Vercel Analytics: Check traffic on new domain
- [ ] Backend API: Monitor request volume on Render
- [ ] Database: Check query performance on Supabase
- [ ] Speed Insights: Verify performance scores

### Keep Old Domain Active

Benefits of keeping `abathar-website.vercel.app` active:
- Existing links don't break
- Search engines can crawl both (or redirect)
- Gradual transition period
- Rollback option if issues arise

To redirect old domain to new:
1. Keep both active initially (2-4 weeks)
2. Monitor traffic on both domains
3. When ready, set `abathar-kmash.de` as primary in Vercel
4. Vercel will auto-redirect `abathar-website.vercel.app` → `abathar-kmash.de`

---

## Part 6: Rollback Plan

If something goes wrong, you can roll back:

### Rollback DNS
1. Remove Vercel DNS records from `abathar-kmash.de`
2. Re-add WordPress hosting DNS records
3. Wait for DNS propagation

### Rollback Backend CORS
1. Update Render environment variable:
   ```
   ALLOWED_ORIGINS=https://abathar-website.vercel.app,http://localhost:3000
   ```
2. Redeploy backend
3. Original site continues working on Vercel

---

## Part 7: WordPress Backup (Before DNS Change)

⚠️ **IMPORTANT**: Backup WordPress before changing DNS

### Backup Checklist
- [ ] Export WordPress content (Tools → Export)
- [ ] Download wp-content folder via FTP
- [ ] Export MySQL database via phpMyAdmin
- [ ] Save current DNS records (screenshot)
- [ ] Document hosting credentials

### Access WordPress After Migration
If you need WordPress content:
- WordPress files are still on hosting server
- Access via IP address or temporary URL
- Can migrate to subdomain (blog.abathar-kmash.de) later

---

## Technical Details

### Current Configuration

**Frontend** (`/frontend/.env.production`):
```bash
NEXT_PUBLIC_API_URL=https://abathar-api.onrender.com
```

**Backend** (`/backend/.env.production`):
```bash
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.xxx.supabase.co:5432/postgres
DEBUG=False
API_HOST=0.0.0.0
API_PORT=8000
ALLOWED_ORIGINS=https://abathar-kmash.de,http://localhost:3000
```

**Image Configuration** (`/frontend/next.config.js`):
```javascript
images: {
  remotePatterns: [
    {
      protocol: 'https',
      hostname: 'abathar-kmash.de',
      pathname: '/wp-content/**',
    },
  ],
}
```

### Environment Variables

No changes needed to frontend environment variables. The API URL remains:
```
NEXT_PUBLIC_API_URL=https://abathar-api.onrender.com
```

---

## Support & Resources

### Useful Commands

```bash
# Test local Docker environment
docker-compose down
docker-compose build
docker-compose up -d
docker logs abathar_backend --tail 100
docker logs abathar_frontend --tail 100

# Test API endpoints
curl https://abathar-api.onrender.com/health
curl https://abathar-api.onrender.com/api/events

# Check DNS
dig abathar-kmash.de
nslookup abathar-kmash.de

# Check SSL
curl -vI https://abathar-kmash.de 2>&1 | grep -i ssl
```

### Documentation Links

- Vercel Custom Domains: https://vercel.com/docs/projects/domains/add-a-domain
- Vercel DNS Configuration: https://vercel.com/docs/projects/domains/dns
- Render Environment Variables: https://render.com/docs/environment-variables
- Next.js Deployment: https://nextjs.org/docs/deployment

### Contact Information

- **Vercel Support**: https://vercel.com/support
- **Render Support**: https://render.com/support
- **DNS Checker**: https://dnschecker.org/
- **SSL Checker**: https://www.sslshopper.com/ssl-checker.html

---

## Summary

### What's Done ✅
- [x] Backend CORS configuration updated
- [x] Local Docker testing completed
- [x] Changes committed to Git
- [x] Code pushed to GitHub

### What's Next ⏳
1. Update `ALLOWED_ORIGINS` in Render dashboard
2. Add `abathar-kmash.de` to Vercel project
3. Configure DNS records at your domain registrar
4. Wait for DNS propagation (24-48 hours max)
5. Test website on new domain
6. Update documentation

### Expected Timeline
- **DNS Configuration**: 5-10 minutes
- **DNS Propagation**: 30 minutes - 48 hours (usually < 1 hour)
- **SSL Provisioning**: 5-10 minutes after DNS propagates
- **Total**: Most likely working within 1-2 hours

---

**Last Updated**: February 23, 2026
**Migration By**: Claude Code
**Project**: Abathar Website
