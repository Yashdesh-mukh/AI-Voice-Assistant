import threading
import tkinter as tk
import uuid
import time

from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from gemini_chat import get_ai_reply
from database import (
    save_db,
    get_all_sessions,
    get_chats_by_session,
    delete_session
)

from ui import AssistantUI
from commands import run_command


session_id = str(uuid.uuid4())
mic_running = True


# -------------------------
# Typing Effect
# -------------------------
def type_ai_text(text):

    for char in text:
        ui.conversation.insert(tk.END, char)
        ui.conversation.update()
        time.sleep(0.02)

    ui.conversation.insert(tk.END, "\n")


# -------------------------
# AI Response Handler
# -------------------------
def respond(reply):

    ui.conversation.insert(tk.END, "AI : ")

    typing_thread = threading.Thread(
        target=type_ai_text,
        args=(reply,)
    )

    speech_thread = threading.Thread(
        target=text_to_speech,
        args=(reply,)
    )

    typing_thread.start()
    speech_thread.start()


# -------------------------
# Voice Logic
# -------------------------
def process_voice():

    try:

        user_text = speech_to_text()

        if not user_text:
            return

        ui.conversation.insert(tk.END, f"\nYou : {user_text}\n")

        command_reply = run_command(user_text)

        if command_reply:
            respond(command_reply)

        else:
            ai_text = get_ai_reply(user_text)
            respond(ai_text)

    except Exception as e:

        print(e)
        ui.conversation.insert(tk.END, "\nAI : Error occurred\n")


# -------------------------
# Continuous Mic
# -------------------------
def listen_continuously():

    while mic_running:

        process_voice()


# -------------------------
# Start Mic Thread
# -------------------------
def start_mic():

    thread = threading.Thread(target=listen_continuously)
    thread.daemon = True
    thread.start()


# -------------------------
# Typing Chat
# -------------------------
def send_text():

    user_text = ui.input_box.get()

    if not user_text:
        return

    ui.conversation.insert(tk.END, f"\nYou : {user_text}\n")

    command_reply = run_command(user_text)

    if command_reply:
        respond(command_reply)

    else:
        ai_text = get_ai_reply(user_text)
        respond(ai_text)

    ui.input_box.delete(0, tk.END)


# -------------------------
# Clear Chat
# -------------------------
def clear_chat():
    ui.conversation.delete("1.0", "end")


# -------------------------
# Delete Session
# -------------------------
def delete_chat():

    selection = ui.history_listbox.curselection()

    if not selection:
        return

    display = ui.history_listbox.get(selection[0])
    session = session_map[display]

    delete_session(session)

    load_history_list()


# -------------------------
# Save Chat
# -------------------------
def save_chat_to_db():

    global session_id

    text = ui.conversation.get("1.0", "end").strip()

    if not text:
        return

    lines = text.split("\n")

    user_text = None

    for line in lines:

        if line.startswith("You :"):
            user_text = line.replace("You :", "").strip()

        elif line.startswith("AI :") and user_text:
            ai_text = line.replace("AI :", "").strip()
            save_db(session_id, user_text, ai_text)
            user_text = None

    ui.conversation.delete("1.0", "end")

    session_id = str(uuid.uuid4())

    load_history_list()


# -------------------------
# Load History
# -------------------------
session_map = {}

def load_history_list():

    sessions = get_all_sessions()

    ui.history_listbox.delete(0, "end")

    for session_id, time in sessions:

        display = time
        session_map[display] = session_id

        ui.history_listbox.insert("end", display)


# -------------------------
# Load Session
# -------------------------
def load_selected_session(event):

    selection = ui.history_listbox.curselection()

    if not selection:
        return

    display = ui.history_listbox.get(selection[0])
    session = session_map[display]

    chats = get_chats_by_session(session)

    ui.conversation.delete("1.0", "end")

    for user_text, ai_text in chats:
        ui.conversation.insert("end", f"You : {user_text}\n")
        ui.conversation.insert("end", f"AI : {ai_text}\n\n")


# -------------------------
# Start App
# -------------------------
ui = AssistantUI(
    None,
    save_chat_to_db,
    load_selected_session,
    send_text,
    clear_chat,
    delete_chat
)

load_history_list()

# start microphone automatically
start_mic()

ui.run()