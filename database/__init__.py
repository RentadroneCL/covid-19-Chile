from os import getenv
from config import env_path
from dotenv import load_dotenv
from orator import DatabaseManager

load_dotenv(dotenv_path=env_path)

config = {
    'sqlite': {
        'driver': getenv('DB_CONNECTION'),
        'database': getenv('DB_DATABASE'),
        'prefix': ''
    }
}

db = DatabaseManager(config)
