import pytest

from python.services.notion import NotionService


def test_notion_service_can_read_database_schema():
    service = NotionService()

    data_source_id = service.get_data_source_id()
    schema = service.get_schema()

    assert data_source_id
    assert isinstance(schema, dict)

    properties = schema.get("properties", {})

    assert len(properties) == 13

    expected_properties = {
        "Name",
        "Email",
        "Company",
        "Industry",
        "Lead Source",
        "Message",
        "Score",
        "Priority",
        "Status",
        "Suggested Action",
        "AI Intent",
        "Business Need",
        "Created At",
    }

    assert expected_properties.issubset(properties.keys())


def test_notion_service_requires_api_key(monkeypatch):
    monkeypatch.setenv("NOTION_API_KEY", "")

    with pytest.raises(ValueError, match="NOTION_API_KEY is not configured"):
        NotionService()


def test_notion_service_requires_database_id(monkeypatch):
    monkeypatch.setenv("NOTION_DATABASE_ID", "")

    with pytest.raises(ValueError, match="NOTION_DATABASE_ID is not configured"):
        NotionService()


def test_notion_service_can_create_lead():
    service = NotionService()

    result = service.create_lead(
        name="Notion Service Test Lead",
        email="notion-service-test@example.com",
        company="Notion Test Company",
        industry="Technology",
        lead_source="Test",
        message="Testing lead creation through the Notion service.",
        score=60,
        priority="High",
        status="New",
        suggested_action="Contact lead",
        ai_intent="Automation inquiry",
        business_need="Lead management automation",
    )

    assert result
    assert result.get("id")
    assert result.get("object") == "page"