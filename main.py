import threading
import tkinter as tk

from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from gemini_chat import get_ai_reply
from save_pdf import save_conversation_pdf
from ui import AssistantUI


# -------------------------
# Background Logic
# -------------------------
def process_voice():
    ui.ask_btn.config(state="disabled")

    try:
        user_text = speech_to_text()

        if user_text == "":
            return

        ui.conversation.insert(tk.END, f"\nYou : {user_text}\n")
        ui.conversation.see(tk.END)

        ai_text = get_ai_reply(user_text)

        ui.conversation.insert(tk.END, f"AI : {ai_text}\n")
        ui.conversation.see(tk.END)

        text_to_speech(ai_text)

    except Exception as e:
        print("Error:", e)
        ui.conversation.insert(tk.END, "\nAI : Something went wrong.\n")
        ui.conversation.see(tk.END)

    finally:
        # This ALWAYS runs
        ui.ask_btn.config(state="normal")


def ask_voice():
    thread = threading.Thread(target=process_voice)
    thread.daemon = True
    thread.start()


def save_pdf():
    save_conversation_pdf(ui.conversation)


# -------------------------
# Start App
# -------------------------
ui = AssistantUI(ask_voice, save_pdf)
ui.run()