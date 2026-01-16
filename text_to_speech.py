import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 230)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

