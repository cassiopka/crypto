def atbash_cipher(text: str) -> str:
    """Атбаш шифр."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    # reversed alphabet
    reverse_alphabet = alphabet[::-1]
    result = ''
    for char in text:
        if char in alphabet:
            # change the symbol 
            index = alphabet.index(char)
            result += reverse_alphabet[index]
        else:
            result += char

    return result

def atbash_decipher(text: str) -> str:
    """Расшифровка атбаш шифра."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    reverse_alphabet = alphabet[::-1]
    result = ''
    for char in text:
        if char in reverse_alphabet:
            # change the symbol 
            index = reverse_alphabet.index(char)
            result += alphabet[index]
        else:
            result += char

    return result
