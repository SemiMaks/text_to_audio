'''
Программа запрашивате название файла (с расширением)
Конвертирует его и зачитывает.
Файл должен быть размещён в папку с самой программой.
'''

from urllib.request import urlopen

import pyttsx3
from gtts import gTTS
from playsound import playsound

from pdf_to_txt import convert

text_val = 'Интернет отсутствует'


def internet_status(file):
    try:
        urlopen("http://google.com")
        print("INFO: Internet OK")

        with open(file, 'r', encoding='utf8') as fin:
            files = fin.read().splitlines()
            with open('out_file.txt', 'w', encoding='utf8') as out_file:
                files = ''.join(files)
                out_file.write(files)

        print('INFO: Преобразование текста....')
        internet_on(files)
    except IOError:
        print("INFO: Неполадки с интернетом!")
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


def main():
    print('Укажите файл:')
    file = input()
    print(file)
    if file.endswith('.txt'):
        print('Обработка txt файла...')
        internet_status(file)
    elif file.endswith('.pdf'):
        print('Конвертирование pdf файла...')
        convert(file)
        internet_status('pdf_out_file.txt')
    else:
        print('Неверное расширение файла...')


main()
