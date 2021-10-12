import speech_recognition as sr

rec = sr.Recognizer()

#Linha de comando para descobrir o nome do microfone e aplicar no parametro with sr.Microphone()
#print(sr.Microphone().list_microphone_names())

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale agora para captar a mensagem")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)