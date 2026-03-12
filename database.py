import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    try:
        password = os.getenv("DB_PASSWORD")

        if not password:
            raise ValueError("DB_PASSWORD not found")

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="ai_assistant"
        )

    except Exception as e:
        print("Database Connection Error:", e)
        return None


def save_db(session_id, user_text, ai_text):
    conn = None
    cursor = None

    try:
        conn = connect_db()
        if not conn:
            return

        cursor = conn.cursor()

        query = """
        INSERT INTO chats (session_id, user_message, ai_message)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (session_id, user_text, ai_text))
        conn.commit()

    except Exception as e:
        print("Database Save Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_all_sessions():
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT session_id
    FROM chats
    GROUP BY session_id
    ORDER BY MAX(created_at) DESC
    """

    cursor.execute(query)
    sessions = cursor.fetchall()

    cursor.close()
    conn.close()

    return [s[0] for s in sessions]


def get_chats_by_session(session_id):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT user_message, ai_message
    FROM chats
    WHERE session_id = %s
    ORDER BY created_at ASC
    """

    cursor.execute(query, (session_id,))
    chats = cursor.fetchall()

    cursor.close()
    conn.close()

    return chats