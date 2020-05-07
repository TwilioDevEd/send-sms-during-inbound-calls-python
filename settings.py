import os
from os.path import join, dirname
from dotenv import load_dotenv  # need to `pip install -U python-dotenv`

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
print(dotenv_path)

# Load file from the path.
load_dotenv(dotenv_path)

# Accessing variables.
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
