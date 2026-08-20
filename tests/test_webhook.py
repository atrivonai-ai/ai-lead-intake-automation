"""
Tests for the webhook API endpoint.
"""

from fastapi.testclient import TestClient

from python.main import app


def test_webhook_accepts_valid_lead():
    """Test that the webhook accepts a valid lead."""

    client = TestClient(app)

    response = client.post(
        "/webhook/lead",
        json={
            "lead": {
                "name": "Webhook Test Lead",
                "email": "webhook@example.com",
                "company": "Webhook Test Company",
                "industry": "Technology",
                "lead_source": "n8n",
                "message": "We want to automate our lead qualification process.",
            }
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_webhook_rejects_invalid_email():
    """Test that the webhook rejects an invalid email address."""

    client = TestClient(app)

    response = client.post(
        "/webhook/lead",
        json={
            "lead": {
                "name": "Invalid Webhook Lead",
                "email": "not-an-email",
                "company": "Test Company",
                "industry": "Technology",
                "lead_source": "n8n",
                "message": "Testing webhook validation.",
            }
        },
    )

    assert response.status_code == 422


def test_webhook_rejects_missing_lead():
    """Test that the webhook rejects a payload without a lead."""

    client = TestClient(app)

    response = client.post(
        "/webhook/lead",
        json={},
    )

    assert response.status_code == 422