from utils.input_formatter import format_input
from utils.text_to_numeric import text_to_numeric 
import numpy as np

keyword = input("Введите ключ-слово: ")
text = input("Введите текст для шифрования: ")

keyword = format_input(keyword)
numeric_text = text_to_numeric(keyword)
numeric_text.sort()

numeric_len = len(numeric_text)

cols = numeric_len

matrix = []

while True:
    row_input = input("Введите числа через пробел (или нажмите Enter для завершения): ")
    if not row_input:
        break
    else:
        row = list(map(int, row_input.split()))
        matrix.append(row)

print(numeric_text)
print(keyword)
print(text)
print(numeric_len)
