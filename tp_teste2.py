import speech_recognition as sr

r  = sr.Recognizer()

PATH = 'WhatsApp-Ptt-2020-06-25-at-22.12.41 (online-audio-converter.com).wav'

with sr.AudioFile(PATH) as source:
    audio = r.record(source)

    print(r.recognize_sphinx(audio))