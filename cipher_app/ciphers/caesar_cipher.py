def caesar_cipher(text: str, key: int) -> str:
    """Цезарь шифр с выбором ключа."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = ''.join(alphabet[(alphabet.index(char) + key) % len(alphabet)] for char in text)
    return encrypted_text


def caesar_decipher(text: str, key: int) -> str:
    """Расшифровка цезарь шифра с выбором ключа."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    decrypted_text = ''.join(alphabet[(alphabet.index(char) - key) % len(alphabet)] for char in text)
    return decrypted_text
