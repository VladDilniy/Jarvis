
import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import subprocess
from datetime import datetime
import time
from random import randint#Рандом для анекдотів

def talke(text): #Голос
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', 'ru')
    for voice in voices:
        if voice.name == 'Aleksandr':
            tts.setProperty('voice', voice.id)
    tts.say(text)
    tts.runAndWait()


def talk(words):#Не видаляти
    print(words) 
    os.system(words) 

talke('Привет')

def command():#Слухає мікрофон в фоні і розпізнає 

    r = sr.Recognizer()


    with sr.Microphone() as source:

            print("Говорите")


            r.adjust_for_ambient_noise(source, duration=1)

            audio = r.listen(source)

    try: 
            zadanie = r.recognize_google(audio, language="ru-RU").lower()
            
            print("Вы сказали: " + zadanie)

    except sr.UnknownValueError:

            print("Я вас не понимаю")
            zadanie = command()

    return zadanie


def makeSomething(zadanie):
        #Браузер 
        if 'браузер' in zadanie:
                talke("Открываю")
                print("Открываю")
                url = 'https://google.com'
                webbrowser.open(url)
        elif 'открой браузер' in zadanie:
                talke("Открываю")
                print("Открываю")
                url = 'https://google.com'
                webbrowser.open(url)
        #YouTube
        elif 'ютуб' in zadanie:
                talke("Открываю")
                print("Открываю")
                url = 'https://google.com'
                url2 = 'https://www.youtube.com/'
                webbrowser.open(url)
                webbrowser.open(url2)
        elif 'youtube' in zadanie:
                talke("Открываю")
                print("Открываю")
                url = 'https://www.youtube.com/'
                webbrowser.open(url)
        #TIME
        elif 'время' in zadanie:
                a = time.strftime("%H and %M", time.localtime())
                talke(a)
                print(a)
        elif 'скажи время' in zadanie:
                a = time.strftime("%H and %M", time.localtime())
                talke(a)
                print(a)
        #Name
        elif "джарвис" in zadanie:
                talke('что')
                print('что?')
        elif "джар" in zadanie:
                talke('что')
                print('что?')
        #Date
        elif 'дата' in zadanie:
                a = time.strftime("%Y-%m-%d", time.localtime())
                talke(a)
                print(a) 
        elif 'назови дату' in zadanie:
                a = time.strftime("%Y-%m-%d", time.localtime())
                talke(a) 
                print(a)
        #Анекдоти
        elif 'анекдот' in zadanie:
                a = randint(1,2)
                if a == 1:
                        talke("Почему системы Microsoft не ставят на ракеты США?")
                        talke("Потому что они вернуться за подтверждением или обновлением")
                        print("Почему системы Microsoft не ставят на ракеты США?")
                        print("Потому что они вернуться за подтверждением или обновлением")
                elif a == 2:
                        talke('Упс...забыл')               
        #...
        elif 'отключись' in zadanie:
                talke("Хорошо,без проблем")
                print("Хорошо,без проблем")
                sys.exit()
        elif 'привет' in zadanie:
                talke("Привет")
                print("Привет!")
        elif 'Сколько тебе лет' in zadanie:
                talke("У компьютеров нету возвраста.Но мне уже,,,,,забыл")
                print("У компьютеров нету возвраста.Но мне уже...забыл")



while True:
	makeSomething(command())
input("Press ENTER to exit")
