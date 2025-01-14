import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Fetch Todoist API key
todoist_api_key = os.getenv("TODOIST_API_KEY")

print("Todoist API Key:", todoist_api_key)

