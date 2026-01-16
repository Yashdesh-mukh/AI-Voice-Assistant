import tkinter as tk
from PIL import Image, ImageTk
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech 
from gemini_chat import get_ai_reply
from save_pdf import save_conversation_pdf


def ask_voice():
    user_text = speech_to_text()

    if user_text == "":
        return

    # Show user message
    conversation.insert(tk.END, f"\nYou :  {user_text}\n")

    # Get AI reply
    ai_text = get_ai_reply(user_text)

    # Show AI reply
    conversation.insert(tk.END, f"AI :  {ai_text}\n")

    conversation.see(tk.END)

    # Speak AI reply
    text_to_speech(ai_text)



root = tk.Tk()
root.title("AI Voice Assistant")
root.geometry("600x550")
root.configure(bg="#eef2ff")
root.resizable(False, False)

# Main Card 
card = tk.Frame(root, bg="white", bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=520)

# Avatar
img = Image.open("avatar.jpg")
img = img.resize((100, 100))
avatar = ImageTk.PhotoImage(img)

avatar_label = tk.Label(card, image=avatar, bg="white")
avatar_label.pack(pady=10)

# Title
title = tk.Label(
    card,
    text="AI Voice Assistant",
    font=("Arial", 16, "bold"),
    bg="white"
)
title.pack(pady=5)

# Conversation Box 
text_frame = tk.Frame(card, bg="white")
text_frame.pack(pady=10)

conversation = tk.Text(
    text_frame,
    width=55,
    height=9,
    font=("Arial", 10),
    bd=1,
    relief="solid"
)
conversation.insert("1.0", "Conversation will appear here...")
conversation.pack()

# Buttons
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack(pady=15)

ask_btn = tk.Button(
    btn_frame,
    text="Ask",
    bg="#6366f1",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    bd=0,
    command=ask_voice
)
ask_btn.grid(row=0, column=0, padx=8)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    bg="#ef4444",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    bd=0,
    command=lambda: conversation.delete("1.0", tk.END)
)
clear_btn.grid(row=0, column=1, padx=8)

send_btn = tk.Button(
    btn_frame,
    text="Save",
    bg="#22c55e",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    bd=0,
    command=lambda: save_conversation_pdf(conversation)
)
send_btn.grid(row=0, column=2, padx=8)

root.mainloop()
