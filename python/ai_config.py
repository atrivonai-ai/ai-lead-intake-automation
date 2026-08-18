"""
AI provider configuration.
"""

import os


AI_API_KEY = os.getenv("AI_API_KEY")
AI_MODEL = os.getenv("AI_MODEL", "default")
