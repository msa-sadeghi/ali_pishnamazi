import os
from dotenv import load_dotenv

load_dotenv(".env")
DB_CONFIG = {
    'host' : os.getenv('DB_HOST', 'localhost'),
    'port' : os.getenv('DB_PORT'),
    'database' : os.getenv('DB_NAME'),
    'user' : os.getenv('DB_USER'),
    'password' : os.getenv('DB_PASSWORD')
}

