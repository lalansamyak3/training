from pathlib import Path

from app.auth.router import router as auth_router
from app.core.config import settings
from app.core.database import Base, engine
from app.core.exceptions import AppError
from app.users import models  # noqa: F401  (registers the table)
from app.users.router import router as users_router
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

# Quick start only. Switch to Alembic migrations before production.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Registration API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppError)
async def app_error_handler(_: Request, exc: AppError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


Path(settings.UPLOAD_DIR).mkdir(exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
