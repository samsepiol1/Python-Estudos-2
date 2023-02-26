import speech_recognition as sr

r  = sr.Recognizer()

with sr.Microphone() as fonte:
    print('Diga Algo')
    audio = r.listen(fonte)

    texto = r.recognize_google(audio,language='pt-BR')

    try:
        print("Você disse algo {}".format(texto))
    except:
        print('Não identifiquei audio')
