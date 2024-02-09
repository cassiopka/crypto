def trithemius_cipher(text: str) -> str:
    """Функция для шифрования текста методом Тритемия."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  
    n = len(alphabet)

    encrypted_text = ''
    for j, char in enumerate(text, start=1):  
        i = alphabet.index(char) + j - 1  
        encrypted_text += alphabet[i % n]  

    return encrypted_text

def trithemius_decipher(text: str) -> str:
    """Функция для расшифровки текста, зашифрованного методом Тритемия."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # русский алфавит
    n = len(alphabet)

    decrypted_text = ''
    for j, char in enumerate(text, start=1):  
        i = alphabet.index(char) - j + 1  
        decrypted_text += alphabet[i % n]  

    return decrypted_text
