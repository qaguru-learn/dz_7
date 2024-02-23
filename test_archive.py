from settings import extract_path
import os
import csv
from pypdf import PdfReader
from openpyxl import load_workbook


def find_file(end):
    """Ищет путь к файлу в архиве, который имеет нужное расширение "end" и возвращает путь к нему"""
    files = os.listdir(extract_path)
    for file in files:
        if file.endswith(end):
            return extract_path + '/' + file


def test_csv():
    """Проверка содержимого csv-файла"""
    file_path = find_file('.csv')
    with open(file_path, 'r') as f:
        reader = list(csv.reader(f))
        second_row = reader[1]

    assert int(second_row[0]) == 1  # проверка значения элемента в первом столбце второй строки
    assert int(second_row[1]) == 30  # проверка значения элемента во втором столбце второй строки


def test_pdf():
    """Проверка содержимого pdf-файла"""
    file_path = find_file('.pdf')
    reader = PdfReader(file_path)
    author = reader.metadata.author
    sheets_count = len(reader.pages)

    assert author == "Ёшкин Кот"  # проверка автора
    assert sheets_count == 69  # проверка количества страниц


def test_xlsx():
    """Проверка содержимого xlsx-файла"""
    workbook = load_workbook(find_file('.xlsx'))
    worksheet = workbook.active
    first_name = worksheet.cell(row=3, column=2).value
    last_name = worksheet.cell(row=3, column=3).value
    rows_count = worksheet.max_row

    assert first_name == 'Mara'
    assert last_name == 'Hashimoto'
    assert rows_count == 51
