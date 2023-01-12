import re

import pdfminer.high_level

from pdfminer.high_level import extract_pages


def convert(file):
    page_len = len(list(extract_pages(file)))
    print(f'Количество страниц в файле: {page_len}\n')
    with open(file, 'rb') as pdf_in:
        pdf_out = open('pdf_row_out.txt', 'w', encoding='utf8')
        pdfminer.high_level.extract_text_to_fp(pdf_in, pdf_out)
        pdf_out.close()
        print('INFO: Конвертирование файла завершено')

    with open('pdf_row_out.txt', 'r', encoding='utf8') as fin:
        files = fin.read().splitlines()
        with open('pdf_out_file.txt', 'w', encoding='utf8') as out_file:
            files = ''.join(files)
            files = re.sub('\W+', ' ', files)
            out_file.write(files)
    print('INFO: Обработка текста, удаление спецсимволов- завершены')
    return ('pdf_out_file.txt')
