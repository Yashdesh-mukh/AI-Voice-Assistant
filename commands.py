import webbrowser
import os

def run_command(text):

    text = text.lower()

    if "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "open google" in text:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open chrome" in text:
        os.system("start chrome")
        return "Opening Chrome"

    elif "open github" in text:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    else:
        return None