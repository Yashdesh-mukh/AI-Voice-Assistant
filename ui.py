import tkinter as tk


class AssistantUI:

    def __init__(self, ask_callback, save_callback, history_callback,
                 send_callback, clear_callback, delete_callback):

        self.root = tk.Tk()
        self.root.title("AI Voice Assistant")
        self.root.geometry("900x550")

        # LEFT SIDE (History)
        left_frame = tk.Frame(self.root, width=250, bg="#1e293b")
        left_frame.pack(side="left", fill="y")

        label = tk.Label(
            left_frame,
            text="Chat History",
            bg="#1e293b",
            fg="white",
            font=("Arial", 14, "bold")
        )
        label.pack(pady=10)

        self.history_listbox = tk.Listbox(left_frame)
        self.history_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.history_listbox.bind("<<ListboxSelect>>", history_callback)

        # RIGHT SIDE
        right_frame = tk.Frame(self.root)
        right_frame.pack(side="right", fill="both", expand=True)

        # Chat area
        self.conversation = tk.Text(right_frame, font=("Arial", 11))
        self.conversation.pack(fill="both", expand=True, padx=10, pady=10)

        # Typing area
        input_frame = tk.Frame(right_frame)
        input_frame.pack(fill="x", padx=10, pady=5)

        self.input_box = tk.Entry(input_frame)
        self.input_box.pack(side="left", fill="x", expand=True)

        send_btn = tk.Button(input_frame, text="Send", command=send_callback)
        send_btn.pack(side="right")

        # Buttons
        btn_frame = tk.Frame(right_frame)
        btn_frame.pack(pady=10)

        self.ask_btn = tk.Button(btn_frame, text="Ask", width=10, command=ask_callback)
        self.ask_btn.grid(row=0, column=0, padx=5)

        save_btn = tk.Button(btn_frame, text="Save", width=10, command=save_callback)
        save_btn.grid(row=0, column=1, padx=5)

        clear_btn = tk.Button(btn_frame, text="Clear", width=10, command=clear_callback)
        clear_btn.grid(row=0, column=2, padx=5)

        delete_btn = tk.Button(btn_frame, text="Delete", width=10, command=delete_callback)
        delete_btn.grid(row=0, column=3, padx=5)

    def run(self):
        self.root.mainloop()