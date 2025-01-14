import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test the variables
print("GOOGLE_CLIENT_SECRET:", os.getenv("#"))
print("TODOIST_API_KEY:", os.getenv("#"))

