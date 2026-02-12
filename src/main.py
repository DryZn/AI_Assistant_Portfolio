import os
from dotenv import load_dotenv

# Load environment variables, for API key
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.api.chat import router as chat_router

# Disable docs in production
ENV = os.getenv("ENV", "development")
docs_url = None if ENV == "production" else "/docs"
redoc_url = None if ENV == "production" else "/redoc"

app = FastAPI(
    title="Portfolio Assistant API",
    description="RAG-powered chatbot for portfolio queries",
    version="1.0.0",
    docs_url=docs_url,
    redoc_url=redoc_url,
)

# CORS configuration
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router, prefix="/api", tags=["chat"])


@app.get("/")
async def root():
    return {"message": "Portfolio Assistant API", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
