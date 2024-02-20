def trithemius_cipher(text: str) -> str:
    """Функция для шифрования текста методом Тритемия."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' 
    n = len(alphabet)
    encrypted_text = ''
    for j, char in enumerate(text, start=1):  # перебираем символы текста, начиная с индекса 1
        i = alphabet.index(char) + j - 1  # находим новый индекс символа
        encrypted_text += alphabet[i % n]  # добавляем зашифрованный символ к зашифрованному тексту
    return encrypted_text

def trithemius_decipher(text: str) -> str:
    """Функция для расшифровки текста, зашифрованного методом Тритемия."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  
    n = len(alphabet)
    decrypted_text = ''
    for j, char in enumerate(text, start=1):  # перебираем символы текста, начиная с индекса 1
        i = alphabet.index(char) - j + 1  # находим новый индекс символа
        decrypted_text += alphabet[i % n]  # добавляем расшифрованный символ к расшифрованному тексту
    return decrypted_text
