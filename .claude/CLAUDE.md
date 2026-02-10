# Abathar Website Development Guidelines

## Testing Workflow

**CRITICAL: ALWAYS test with Docker Compose before committing/pushing changes**

This workflow is mandatory to prevent production errors and ensure all changes work correctly before deployment.

### Steps:

1. **Make code changes locally**
   - Edit files as needed
   - Save all changes

2. **Stop running containers**
   ```bash
   docker-compose down
   ```

3. **Rebuild containers** (especially if backend code changed)
   ```bash
   docker-compose build
   ```
   Or rebuild specific service:
   ```bash
   docker-compose build backend
   ```

4. **Start containers**
   ```bash
   docker-compose up -d
   ```

5. **Check logs for errors**
   ```bash
   docker logs abathar_backend --tail 100
   docker logs abathar_frontend --tail 100
   docker logs abathar_db --tail 50
   ```

6. **Test APIs and functionality**
   - Test relevant API endpoints with curl or browser
   - Example: `curl http://localhost:8000/api/videos/featured`
   - Verify frontend at http://localhost:3000
   - Check database with pgAdmin at http://localhost:5050

7. **Only after successful local testing: commit and push**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push
   ```

### Why This Matters

- Prevents syntax errors from reaching production
- Catches database schema issues early
- Verifies environment variables work correctly
- Ensures CORS and API configurations are correct
- Saves time by catching bugs before deployment

### Example: Recent Incident

A syntax error in `seed_data.py` (unmatched `]`) caused production deployment to fail. This could have been caught with local Docker testing before pushing.

## Environment Variables

### Local Development (docker-compose.yml)
- `FORCE_RESEED`: Set to `"true"` temporarily when testing database schema changes
- Remove after testing to preserve data between restarts

### Production (Render)
- `FORCE_RESEED`: Set to `true` only when deploying schema changes
- Remove immediately after successful deployment to prevent data loss

## Database Management

### Force Reseed
When database schema changes (new columns, tables, etc.):

1. Set `FORCE_RESEED=true` in environment
2. Deploy/restart application
3. Verify data is seeded correctly
4. **Immediately remove** `FORCE_RESEED` to prevent accidental data deletion

### Seed Data Updates
When updating seed data (e.g., video titles):

1. Edit `backend/seed_data.py`
2. Test locally with FORCE_RESEED
3. Verify data in local database via pgAdmin
4. Test API endpoints
5. Commit and push
6. Set FORCE_RESEED on production
7. Deploy
8. Verify production data
9. Remove FORCE_RESEED from production

## Project Structure

- `/backend` - FastAPI backend with PostgreSQL
- `/frontend` - Next.js frontend
- `docker-compose.yml` - Local development environment
- `.github/workflows` - CI/CD pipelines
