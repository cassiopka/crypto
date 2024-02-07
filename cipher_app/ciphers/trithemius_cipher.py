def trithemius_cipher(text: str) -> str:
    """Функция для шифрования текста методом Тритемия."""
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # русский алфавит
    n = len(alphabet)

    encrypted_text = ''
    for j, char in enumerate(text, start=1):  # проходим по каждому символу в тексте
        i = alphabet.index(char) + j - 1  # вычисляем новый индекс символа с учетом сдвига
        encrypted_text += alphabet[i % n]  # добавляем зашифрованный символ к результату

    return encrypted_text

def trithemius_decipher(text: str) -> str:
    """Функция для расшифровки текста, зашифрованного методом Тритемия."""
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # русский алфавит
    n = len(alphabet)

    decrypted_text = ''
    for j, char in enumerate(text, start=1):  # проходим по каждому символу в тексте
        i = alphabet.index(char) - j + 1  # вычисляем исходный индекс символа с учетом сдвига
        decrypted_text += alphabet[i % n]  # добавляем расшифрованный символ к результату

    return decrypted_text
