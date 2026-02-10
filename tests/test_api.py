import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from fastapi.testclient import TestClient
from src.main import app


class TestAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup mock for all tests"""
        with patch("src.app.api.chat.get_gemini_service") as mock_get_service:
            # Create mock service
            mock_service = MagicMock()
            mock_service.get_response = AsyncMock(
                return_value={"answer": "Test response", "sources": ["test.md"]}
            )
            mock_service.memory.clear = MagicMock()

            mock_get_service.return_value = mock_service
            self.client = TestClient(app)
            yield

    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

    def test_chat_endpoint_validation(self):
        """Test chat endpoint input validation"""
        # Test missing message - this should always work (Pydantic validation)
        response = self.client.post("/api/chat", json={})
        assert response.status_code == 422

    def test_chat_endpoint_success(self):
        """Test successful chat endpoint"""
        response = self.client.post("/api/chat", json={"message": "Hello"})
        assert response.status_code == 200
        data = response.json()
        assert data["response"] == "Test response"
        assert data["sources"] == ["test.md"]

    def test_reset_endpoint(self):
        """Test conversation reset endpoint"""
        response = self.client.post("/api/chat/reset")
        assert response.status_code == 200
        assert response.json() == {"message": "Conversation reset successfully"}
