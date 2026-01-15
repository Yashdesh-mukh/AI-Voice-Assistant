import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 230)


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


