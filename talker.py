from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

#ambobs  audioshi rasac gadavcemt  argumentad

def talkToMe (audio):
    print(audio)
    tts=gTTs(text-audio, lang="en")
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

#qomandi imistvis ro momisminos

def mycomand ():
    r = sr.recognizer()

    with sr.microphone() as source:
        print ("your slave is ready to listen to you ")
        r.pause_threshold = 2
        r.adjust_ambient_noise(source, duration = 2  )
        audio=r.listen (source)
    try:
        command=r.recognize_google(audio)
        print (" shen mitxari" + command+"\n")

    #loop avs mosmenas ro gaagrdzelos mosmena tu ver mixvda ra vitxarit comandshi
    except sr.UnknownValueError:
        asistent(mycomand())
    return comand

#if ebi brdzanebebistvis
def assistant(comand):
    if "open facebook" in comand:
        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application"
        url= "facebook.com"
        webbrowser.get(chrome_path).opem(url)
    elif "what\'s up" in comand:
        talkToMe(" helping you master")
    elif "mail"in comand:
        talkToMe("recipient is ?" )
        recipient = mycomand()
        if "george" is recipient :
            talkToMe("what should i text him")
            content = mycomand()

             #send mail s vutitebt

            mail=smtplib.SMPT ("smtp.gmail.com",587)

             #serveris identifikacia
            mail.elho()

            #encription

            mail.starttls()

            #avtorizacia meilze

            mail.login("username" , "password")

            #mesijis gagzavna

            mail.sendmail("person name" , "example@mail.ge" , content)

            #kavshiris dasruleba

            mail.close()
            talkToMe("Email sent")


