# Project Context

## Architecture
- Backend: Django Rest Framework (DRF)
- Frontend: NextJS
- Server: Nginx (configuration at `backend/docker/local/nginx/default.conf`)
- Database: PostgreSQL
- Container Orchestration: Docker Compose

## Development Environment
- All services run in Docker containers
- Custom Docker network: `dealsmo_nw`
- Project is managed via Makefile commands

## Key Makefile Commands
```bash
make build          # Build and start all containers
make up            # Start containers
make down          # Stop containers
make migrate       # Run Django migrations
make frontend      # Rebuild and restart frontend
make superuser     # Create Django superuser
make collectstatic # Collect Django static files
```

## Important Paths
- Nginx config: `backend/docker/local/nginx/default.conf`
- Docker Compose: `local.yml`
- Frontend: `frontend/`
- Backend: `backend/`

## Development Workflow
1. All commands should be executed through Docker and Makefile
2. Frontend and backend communicate through Nginx reverse proxy
3. Database operations are performed through Docker containers
4. Frontend hot-reloading and backend development server are configured through Docker 