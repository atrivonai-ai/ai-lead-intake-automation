"""
Tests for the FastAPI application configuration.
"""

from python.main import app


def test_application_title():
    """Test that the FastAPI application has the expected title."""

    assert app.title == "AI Lead Intake and Qualification Automation"


def test_application_version():
    """Test that the API version is configured correctly."""

    assert app.version == "1.0.0"
