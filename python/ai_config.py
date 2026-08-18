"""
AI provider configuration.
"""

from dotenv import load_dotenv
import os


load_dotenv()


AI_API_KEY = os.getenv("AI_API_KEY")
AI_MODEL = os.getenv("AI_MODEL")

if AI_MODEL is None or not AI_MODEL.strip():
    AI_MODEL = "default"