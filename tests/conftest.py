"""
Shared pytest fixtures for the AI Lead Intake and Qualification Automation.
"""

import pytest
from fastapi.testclient import TestClient

from python.main import app


@pytest.fixture
def client() -> TestClient:
    """Return a FastAPI test client."""

    return TestClient(app)
