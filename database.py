import sqlite3


conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    session_id TEXT,
    user_text TEXT,
    ai_text TEXT
)
""")

conn.commit()
conn.close()


# Save chat
def save_db(session_id, user_text, ai_text):

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats VALUES (?, ?, ?)",
        (session_id, user_text, ai_text)
    )

    conn.commit()
    conn.close()


# Get sessions
def get_all_sessions():

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT session_id FROM chats")

    rows = cursor.fetchall()

    conn.close()

    return [r[0] for r in rows]


# Get chats
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


# Delete session
def delete_session(session):

    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM chats WHERE session_id=?",
        (session,)
    )

    conn.commit()
    conn.close()