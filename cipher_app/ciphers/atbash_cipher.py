

def atbash_cipher(text: str) -> str:
    """Атбаш шифр."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    reverse_alphabet = alphabet[::-1] # переворачиваем алфавит 
    result = ''
    for char in text:  # проходимся по каждому символу в тексте
        if char in alphabet:  # если символ присутствует в алфавите
            index = alphabet.index(char)  # найдем его индекс
            result += reverse_alphabet[index]  # добавим в результат соответствующий символ из перевернутого алфавита
        else:
            result += char
    return result

def atbash_decipher(text: str) -> str:
    """Расшифровка атбаш шифра."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    reverse_alphabet = alphabet[::-1]
    result = '' 
    for char in text:  # проходимся по каждому символу в тексте
        if char in reverse_alphabet:  # если символ присутствует в перевернутом алфавите
            index = reverse_alphabet.index(char)  # найдем его индекс
            result += alphabet[index]  # добавим в результат соответствующий символ из обычного алфавита
        else:
            result += char 
    return result  

