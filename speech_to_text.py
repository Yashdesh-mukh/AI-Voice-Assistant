import speech_recognition as sr

r = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
       
        print("Calibrating for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something...")
        
      
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Google could not understand audio either.")
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
        

