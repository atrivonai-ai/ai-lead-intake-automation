"""
Tests for the lead API endpoints.
"""

from fastapi.testclient import TestClient

from python.api import leads
from python.main import app


def test_health_endpoint():
    """Test that the health endpoint responds correctly."""

    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_process_lead_endpoint(monkeypatch):
    """Test that the lead processing endpoint accepts a valid lead."""

    class FakeResult:
        priority = "high"

    monkeypatch.setattr(
        leads,
        "process_lead",
        lambda lead: FakeResult(),
    )

    client = TestClient(app)

    response = client.post(
        "/leads/process",
        json={
            "name": "Sarah Johnson",
            "email": "sarah@example.com",
            "company": "BrightTech",
            "industry": "Technology",
            "lead_source": "Referral",
            "message": "We want to automate our lead management process.",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Lead processed with high priority.",
        "status": "success",
    }


def test_process_lead_rejects_invalid_email():
    """Test that an invalid email is rejected."""

    client = TestClient(app)

    response = client.post(
        "/leads/process",
        json={
            "name": "Sarah Johnson",
            "email": "not-an-email",
            "company": "BrightTech",
            "industry": "Technology",
            "lead_source": "Referral",
            "message": "We want to automate our lead management process.",
        },
    )

    assert response.status_code == 422


def test_process_lead_rejects_missing_message():
    """Test that a missing required message is rejected."""

    client = TestClient(app)

    response = client.post(
        "/leads/process",
        json={
            "name": "Sarah Johnson",
            "email": "sarah@example.com",
            "company": "BrightTech",
            "industry": "Technology",
            "lead_source": "Referral",
        },
    )

    assert response.status_code == 422
