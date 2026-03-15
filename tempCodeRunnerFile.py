import threading
import tkinter as tk
import uuid

from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from gemini_chat import get_ai_reply
from database import (
    save_db,
    get_all_sessions,
    get_chats_by_session
)
from ui import AssistantUI
from commands import run_command


# Generate new session when app starts
session_id = str(uuid.uuid4())


# -------------------------
# Voice Logic
# -------------------------
def process_voice():
    ui.ask_btn.config(state="disabled")

    try:
        user_text = speech_to_text()

        if not user_text:
            return

        ui.conversation.insert(tk.END, f"\nYou : {user_text}\n")
        command_reply = run_command(user_text)
        if command_reply:
              ui.conversation.insert(tk.END, f"AI : {command_reply}\n")
              text_to_speech(command_reply)
        else:
            ai_text = get_ai_reply(user_text)
            ui.conversation.insert(tk.END, f"AI : {ai_text}\n")
            text_to_speech(ai_text)

    except Exception as e:
        print("Error:", e)
        ui.conversation.insert(tk.END, "\nAI : Something went wrong.\n")

    finally:
        ui.ask_btn.config(state="normal")


def ask_voice():
    thread = threading.Thread(target=process_voice)
    thread.daemon = True
    thread.start()


# -------------------------
# Save Current Session
# -------------------------
def save_chat_to_db():
    global session_id

    full_text = ui.conversation.get("1.0", "end-1c").strip()

    if not full_text:
        return

    lines = full_text.split("\n")
    user_text = None

    for line in lines:
        if line.startswith("You :"):
            user_text = line.replace("You :", "").strip()

        elif line.startswith("AI :") and user_text:
            ai_text = line.replace("AI :", "").strip()
            save_db(session_id, user_text, ai_text)
            user_text = None

    # Clear chat after saving
    ui.conversation.delete("1.0", "end")

    # Generate new session
    session_id = str(uuid.uuid4())

    # Refresh history sidebar
    load_history_list()


# Load History List

def load_history_list():
    sessions = get_all_sessions()

    ui.history_listbox.delete(0, "end")

    for s in sessions:
        ui.history_listbox.insert("end", s)



# Load Selected Session

def load_selected_session(event):
    selection = ui.history_listbox.curselection()

    if not selection:
        return

    selected_session = ui.history_listbox.get(selection[0])

    chats = get_chats_by_session(selected_session)

    ui.conversation.delete("1.0", "end")

    for user_text, ai_text in chats:
        ui.conversation.insert("end", f"You : {user_text}\n")
        ui.conversation.insert("end", f"AI : {ai_text}\n\n")


# Start App

ui = AssistantUI(ask_voice, save_chat_to_db, load_selected_session)

load_history_list()

ui.run()