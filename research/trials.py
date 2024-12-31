import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key
google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = google_api_key

# Verify that the key is loaded
if google_api_key:
    print("Google API key loaded successfully!")
else:
    print("Failed to load the Google API key.")

print(google_api_key)