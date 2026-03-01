import tkinter as tk
from PIL import Image, ImageTk


class AssistantUI:
    def __init__(self, ask_callback, save_callback):
        self.root = tk.Tk()
        self.root.title("AI Voice Assistant")
        self.root.geometry("600x550")
        self.root.configure(bg="#eef2ff")
        self.root.resizable(False, False)

        # Main Card
        card = tk.Frame(self.root, bg="white", bd=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=520)

        # Avatar
        img = Image.open("avatar.jpg")
        img = img.resize((100, 100))
        self.avatar = ImageTk.PhotoImage(img)

        avatar_label = tk.Label(card, image=self.avatar, bg="white")
        avatar_label.pack(pady=10)

        # Title
        title = tk.Label(
            card,
            text="AI Voice Assistant",
            font=("Arial", 16, "bold"),
            bg="white"
        )
        title.pack(pady=5)

        # Text Frame
        text_frame = tk.Frame(card, bg="white")
        text_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(text_frame)

        self.conversation = tk.Text(
            text_frame,
            width=55,
            height=10,
            font=("Arial", 10),
            bd=1,
            relief="solid",
            wrap="word",
            yscrollcommand=scrollbar.set
        )

        scrollbar.config(command=self.conversation.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.conversation.pack(side=tk.LEFT)

        self.conversation.insert("1.0", "Click Ask and start speaking...\n")

        # Buttons
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(pady=15)

        self.ask_btn = tk.Button(
            btn_frame,
            text="Ask",
            bg="#6366f1",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            bd=0,
            command=ask_callback
        )
        self.ask_btn.grid(row=0, column=0, padx=8)

        clear_btn = tk.Button(
            btn_frame,
            text="Clear",
            bg="#ef4444",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            bd=0,
            command=lambda: self.conversation.delete("1.0", tk.END)
        )
        clear_btn.grid(row=0, column=1, padx=8)

        save_btn = tk.Button(
            btn_frame,
            text="Save",
            bg="#22c55e",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            bd=0,
            command=save_callback
        )
        save_btn.grid(row=0, column=2, padx=8)

    def run(self):
        self.root.mainloop()