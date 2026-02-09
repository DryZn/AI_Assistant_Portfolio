# Portfolio Assistant API - Backend

RAG (Retrieval Augmented Generation) API for professional portfolio chatbot.

## 🚀 Technologies

- **Framework**: FastAPI
- **LLM**: OpenAI GPT-4
- **RAG**: LangChain + FAISS
- **Embeddings**: OpenAI text-embedding-3-small

## 📦 Installation

```bash
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Activate environment (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```

2. Add your OpenAI API key in `.env`:
```
OPENAI_API_KEY=sk-...
```

## 🏃 Run Server

```bash
# Development mode with auto-reload
uvicorn main:app --reload --port 8000

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

API will be accessible at `http://localhost:8000`

## 📚 API Documentation

Once server is running, access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔌 Endpoints

### POST `/api/chat`
Send a message to the chatbot

**Request:**
```json
{
  "message": "Tell me about your experience at Ericsson"
}
```

**Response:**
```json
{
  "response": "I worked 4+ years at Ericsson...",
  "sources": ["data/experience-ericsson.md"]
}
```

### POST `/api/chat/reset`
Reset conversation

### GET `/health`
Check API health status

## 📁 Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── chat.py          # Chat endpoints
│   └── services/
│       └── rag_service.py   # RAG service
├── data/
│   ├── cv.md                # Resume
│   ├── experience-ericsson.md
│   ├── projects.md
│   └── skills.md
├── main.py                  # FastAPI application
├── requirements.txt
└── .env.example
```

## 🧪 Testing

```bash
# Test API with curl
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What are your Python skills?"}'
```

## 🚀 Deployment

### Railway

1. Create account on [Railway](https://railway.app)
2. Connect your GitHub repo
3. Add `OPENAI_API_KEY` environment variable
4. Railway will automatically detect FastAPI

### Render

1. Create account on [Render](https://render.com)
2. Create new Web Service
3. Connect your repo
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add `OPENAI_API_KEY` environment variable

## 📝 Customization

To customize chatbot data, modify files in `data/`:
- `cv.md`: Resume information
- `experience-ericsson.md`: Professional experience details
- `projects.md`: Completed projects
- `skills.md`: Technical skills

RAG system will automatically reload documents on next startup.

## 🔧 Development

### Add new endpoints

Create a new router in `app/api/` and include it in `main.py`.

### Modify RAG behavior

Adjust parameters in `app/services/rag_service.py`:
- `chunk_size`: Text chunk size
- `chunk_overlap`: Overlap between chunks
- `k`: Number of documents to retrieve
- `temperature`: Response creativity

## 📧 Support

For questions: lesenfans.anthony@gmail.com
