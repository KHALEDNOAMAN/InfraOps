from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import datacenter, assets, lifecycle, capacity, changes, auth

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="InfraOps Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(datacenter.router, prefix="/datacenters", tags=["datacenters"])
app.include_router(assets.router, prefix="/assets", tags=["assets"])
app.include_router(lifecycle.router, prefix="/lifecycle", tags=["lifecycle"])
app.include_router(capacity.router, prefix="/capacity", tags=["capacity"])
app.include_router(changes.router, prefix="/changes", tags=["changes"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}
