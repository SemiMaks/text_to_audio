# Программ зачитывает текс

from urllib.request import urlopen

import pyttsx3
from gtts import gTTS
from playsound import playsound

text_val = 'Welcom to python'
text_rus = 'Я говорю на русском'


def internet_status(file):
    try:
        urlopen("http://google.com")
        print("INFO: Internet OK")
        file_text = []
        with open(file, 'r', encoding='utf8') as fin:
            for line in fin:
                file_text.append(line)
                file_text = ''.join(file_text)
        print(file_text)
        internet_on(file_text)
    except IOError:
        print("INFO: Internet is broken!")
        internet_off(text_val)


def internet_on(file_text):
    language = 'ru'
    obj = gTTS(text=file_text, lang=language, slow=False)
    obj.save("txt_to_audio.mp3")
    playsound("txt_to_audio.mp3")


def internet_off(text_val):
    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1)
    engine.say(text_val)
    engine.runAndWait()


def main(dir_path):
    print('Укажите файл:')
    file = input()
    internet_status(file)


main('text.txt')
