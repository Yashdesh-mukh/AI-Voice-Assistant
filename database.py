import mysql.connector
from dotenv import load_dotenv

def connect_db():
    return mysql.connector.connect(
        host = 'localhost',
        user = "root"
        password = os.getenv("DB_PASSWORD"),
        database = "ai_assistant"
        )
    