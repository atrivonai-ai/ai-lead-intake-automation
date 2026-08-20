from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any

from dotenv import load_dotenv


class NotionService:
    """Service responsible for communicating with the Notion API."""

    NOTION_API_URL = "https://api.notion.com/v1"
    NOTION_VERSION = "2026-03-11"

    def __init__(self) -> None:
        load_dotenv()

        self.api_key = os.getenv("NOTION_API_KEY")
        self.database_id = os.getenv("NOTION_DATABASE_ID")

        if not self.api_key:
            raise ValueError("NOTION_API_KEY is not configured.")

        if not self.database_id:
            raise ValueError("NOTION_DATABASE_ID is not configured.")

        self._data_source_id: str | None = None

    def _request(
        self,
        path: str,
        method: str = "GET",
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Send an authenticated request to the Notion API."""

        url = f"{self.NOTION_API_URL}{path}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.NOTION_VERSION,
            "Content-Type": "application/json",
        }

        data = None

        if payload is not None:
            data = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers=headers,
        )

        try:
            with urllib.request.urlopen(request) as response:
                response_body = response.read().decode("utf-8")

                if not response_body:
                    return {}

                return json.loads(response_body)

        except urllib.error.HTTPError as error:
            error_body = error.read().decode("utf-8")

            raise RuntimeError(
                f"Notion API request failed with status "
                f"{error.code}: {error_body}"
            ) from error

    def get_data_source_id(self) -> str:
        """Return the data source associated with the configured database."""

        if self._data_source_id:
            return self._data_source_id

        database = self._request(
            f"/databases/{self.database_id}"
        )

        data_sources = database.get("data_sources", [])

        if not data_sources:
            raise RuntimeError(
                "No data source was found for the configured Notion database."
            )

        self._data_source_id = data_sources[0]["id"]

        return self._data_source_id

    def get_schema(self) -> dict[str, Any]:
        """Return the schema of the configured Notion data source."""

        data_source_id = self.get_data_source_id()

        return self._request(
            f"/data_sources/{data_source_id}"
        )

    def create_lead(
        self,
        name: str,
        email: str,
        company: str,
        industry: str,
        lead_source: str,
        message: str,
        score: int,
        priority: str,
        status: str,
        suggested_action: str,
        ai_intent: str,
        business_need: str,
        created_at: datetime | None = None,
    ) -> dict[str, Any]:
        """Create a lead record in the configured Notion database."""

        data_source_id = self.get_data_source_id()

        if created_at is None:
            created_at = datetime.now(timezone.utc)

        payload = {
            "parent": {
                "data_source_id": data_source_id
            },
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": name
                            }
                        }
                    ]
                },
                "Email": {
                    "email": email
                },
                "Company": {
                    "rich_text": [
                        {
                            "text": {
                                "content": company
                            }
                        }
                    ]
                },
                "Industry": {
                    "rich_text": [
                        {
                            "text": {
                                "content": industry
                            }
                        }
                    ]
                },
                "Lead Source": {
                    "rich_text": [
                        {
                            "text": {
                                "content": lead_source
                            }
                        }
                    ]
                },
                "Message": {
                    "rich_text": [
                        {
                            "text": {
                                "content": message
                            }
                        }
                    ]
                },
                "Score": {
                    "number": score
                },
                "Priority": {
                    "select": {
                        "name": priority
                    }
                },
                "Status": {
                    "select": {
                        "name": status
                    }
                },
                "Suggested Action": {
                    "rich_text": [
                        {
                            "text": {
                                "content": suggested_action
                            }
                        }
                    ]
                },
                "AI Intent": {
                    "rich_text": [
                        {
                            "text": {
                                "content": ai_intent
                            }
                        }
                    ]
                },
                "Business Need": {
                    "rich_text": [
                        {
                            "text": {
                                "content": business_need
                            }
                        }
                    ]
                },
                "Created At": {
                    "date": {
                        "start": created_at.isoformat()
                    }
                },
            },
        }

        return self._request(
            "/pages",
            method="POST",
            payload=payload,
        )