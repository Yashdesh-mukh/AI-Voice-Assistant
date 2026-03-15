import sqlite3
from datetime import datetime

conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    session_id TEXT,
    user_text TEXT,
    ai_text TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()


def save_db(session_id, user_text, ai_text):

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    time = datetime.now().strftime("%d-%m-%Y %H:%M")

    cursor.execute(
        "INSERT INTO chats VALUES (?, ?, ?, ?)",
        (session_id, user_text, ai_text, time)
    )

    conn.commit()
    conn.close()


def get_all_sessions():

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT session_id, MIN(time)
    FROM chats
    GROUP BY session_id
    ORDER BY time DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_chats_by_session(session):

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_text, ai_text FROM chats WHERE session_id=?",
        (session,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_session(session):

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM chats WHERE session_id=?",
        (session,)
    )

    conn.commit()
    conn.close()