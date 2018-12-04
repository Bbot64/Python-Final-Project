import pyttsx3

def voice(s):
    engine = pyttsx3.init()
    engine.say(s)
    engine.runAndWait()

#I installed pyttsx3 pywin32 and pypiwin32
