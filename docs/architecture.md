# Architecture Overview
InfraOps follows a modern 3-tier architecture.

## Frontend
React + TypeScript + Vite, using TailwindCSS for styling and Recharts for data visualization. State is managed via React Context.

## Backend
FastAPI (Python) providing a RESTful API. SQLAlchemy for ORM. Celery + Redis for background tasks (e.g. SNMP polling).

## Database
PostgreSQL 14 for relational data storage. Redis for caching and task queues.
