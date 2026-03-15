import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    recognizer.adjust_for_ambient_noise(source)


def speech_to_text():

    with mic as source:

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            text = recognizer.recognize_google(audio)

            print("You said:", text)

            return text

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            return None