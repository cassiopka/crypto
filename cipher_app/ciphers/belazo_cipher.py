def belazo_cipher(text: str, key: str) -> str:
    """Шифр Белазо."""
    # Создаем таблицу алфавита, каждая строка - сдвиг на 1 букву
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Преобразование текста и ключа в нижний регистр
    text = text.lower()
    key = key.lower()

    # Шифрование текста
    encrypted_text = ''
    for i, char in enumerate(text):
        if char in alphabet:
            # Находим сдвиг алфавита для текущей буквы ключа
            shift = alphabet.index(key[i % len(key)])
            # Находим букву в алфавите с учетом сдвига
            encrypted_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def belazo_decipher(text: str, key: str) -> str:
    """Дешифрование шифра Белазо."""
    # Создаем таблицу алфавита, каждая строка - сдвиг на 1 букву
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Преобразование текста и ключа в нижний регистр
    text = text.lower()
    key = key.lower()

    # Расшифрованный текст
    decrypted_text = ''
    for i, char in enumerate(text):
        if char in alphabet:
            # Находим сдвиг алфавита для текущей буквы ключа
            shift = alphabet.index(key[i % len(key)])
            # Находим букву в алфавите с учетом обратного сдвига
            decrypted_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text
