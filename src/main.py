from dotenv import load_dotenv

# Load environment variables, for API key
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.api.chat import router as chat_router

app = FastAPI(
    title="Portfolio Assistant API",
    description="RAG-powered chatbot for portfolio queries",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure with your frontend URL in production
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
