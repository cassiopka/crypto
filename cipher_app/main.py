from ciphers.atbash_cipher import atbash_cipher, atbash_decipher
from ciphers.caesar_cipher import caesar_cipher, caesar_decipher
from ciphers.polybius_square_cipher import polybius_square_cipher, polybius_square_decipher
from ciphers.trithemius_cipher import trithemius_cipher, trithemius_decipher
from ciphers.belazo_cipher import belazo_cipher, belazo_decipher
from ciphers.matrix_cipher import *

from utils.input_formatter import format_input
from utils.block_formatter import format_blocks
from utils.print_square import print_polybius_square
from utils.text_to_numeric import text_to_numeric

def input_key_matrix(size):
    """Функция для ввода ключевой матрицы."""
    key_matrix = []

    print("Введите элементы ключевой матрицы построчно:")
    for _ in range(size):
        row = list(map(int, input().split()))
        key_matrix.append(row)

    return np.array(key_matrix)


def main():
    while True:
        print("Выберите действие:")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("0. Выйти")

        action_choice = input("Введите номер действия: ")

        if action_choice == '0':
            print("Выход из программы.")
            break

        if action_choice not in ['1', '2']:
            print("Неверный выбор действия!")
            continue

        if action_choice == '1':
            cipher_mode = 'зашифровать'
        elif action_choice == '2':
            cipher_mode = 'расшифровать'

        print("Выберите шифр:")
        print("1. Атбаш")
        print("2. Цезарь")
        print("3. Квадрат Полибия")
        print("4. Тритемия")
        print("5. Белазо")
        print("6. Матричный шифр")

        cipher_choice = input("Введите номер шифра: ")

        if cipher_choice not in ['1', '2', '3', '4', '5', '6']:
            print("Неверный выбор шифра!")
            continue

        if cipher_choice == '3':
            print_polybius_square()

        text = input(f"Введите текст для {cipher_mode}: ")

        formatted_text = format_input(text)

        if cipher_choice == '1':
            if action_choice == '1':
                result = atbash_cipher(formatted_text)
            else:
                result = atbash_decipher(formatted_text)
        elif cipher_choice == '2':
            if action_choice == '1':
                key = int(input("Введите ключ для Цезаря: "))
                result = caesar_cipher(formatted_text, key)
            else:
                key = int(input("Введите ключ для Цезаря: "))
                result = caesar_decipher(formatted_text, key)
        elif cipher_choice == '3':
            if action_choice == '1':
                result = polybius_square_cipher(formatted_text)
            else:
                result = polybius_square_decipher(formatted_text)
        elif cipher_choice == '4':
            if action_choice == '1':
                result = trithemius_cipher(formatted_text)
            else:
                result = trithemius_decipher(formatted_text)
        elif cipher_choice == '5':
            key = input("Введите ключ для шифра Белазо: ")
            if action_choice == '1':
                result = belazo_cipher(formatted_text, key)
            else:
                result = belazo_decipher(formatted_text, key)
        elif cipher_choice == '6':
            key_size = int(input("Введите размер ключевой матрицы: "))
            key_matrix = input_key_matrix(key_size)
            text_numeric = text_to_numeric(formatted_text)
            if action_choice == '1':
                result = matrix_cipher(text_numeric, key_matrix)
            else:
                result = matrix_decipher(text, key_matrix)
            print(result)

        formatted_result = format_blocks(result)

        print("Результат:")
        print(formatted_result)

if __name__ == "__main__":
    main()

