import tkinter as tk


class AssistantUI:
    def __init__(self, ask_callback, save_callback, history_select_callback):

        self.root = tk.Tk()
        self.root.title("AI Voice Assistant")
        self.root.geometry("900x550")
        self.root.configure(bg="#eef2ff")

        # LEFT PANEL (History)
        left_frame = tk.Frame(self.root, bg="#1e293b", width=250)
        left_frame.pack(side="left", fill="y")

        history_label = tk.Label(
            left_frame,
            text="Chat History",
            fg="white",
            bg="#1e293b",
            font=("Arial", 14, "bold")
        )
        history_label.pack(pady=10)

        self.history_listbox = tk.Listbox(
            left_frame,
            bg="white",
            width=30
        )
        self.history_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.history_listbox.bind("<<ListboxSelect>>", history_select_callback)

        # RIGHT PANEL (Chat)
        right_frame = tk.Frame(self.root, bg="white")
        right_frame.pack(side="right", fill="both", expand=True)

        self.conversation = tk.Text(
            right_frame,
            font=("Arial", 11),
            wrap="word"
        )
        self.conversation.pack(fill="both", expand=True, padx=15, pady=15)

        btn_frame = tk.Frame(right_frame, bg="white")
        btn_frame.pack(pady=10)

        self.ask_btn = tk.Button(
            btn_frame,
            text="Ask",
            bg="#6366f1",
            fg="white",
            width=12,
            command=ask_callback
        )
        self.ask_btn.grid(row=0, column=0, padx=8)

        save_btn = tk.Button(
            btn_frame,
            text="Save",
            bg="#22c55e",
            fg="white",
            width=12,
            command=save_callback
        )
        save_btn.grid(row=0, column=1, padx=8)

    def run(self):
        self.root.mainloop()