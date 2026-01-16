from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime
import tkinter as tk
import os

def save_conversation_pdf(conversation):
    text = conversation.get("1.0", tk.END).strip()

    if text == "":
        return

    # Folder name
    folder_name = "conversations"

    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # File name with date & time
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder_name, f"conversation_{now}.pdf")

    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    x = 40
    y = height - 50

    c.setFont("Helvetica", 10)

    for line in text.split("\n"):
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = height - 50

        c.drawString(x, y, line)
        y -= 15

    c.save()
