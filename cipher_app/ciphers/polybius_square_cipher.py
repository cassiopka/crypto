# polybius_square_cipher.py

def polybius_square_cipher(text: str) -> str:
    """Квадрат Полибия."""
    # letters with keys (ij)  
    polybius_table = {
        'а': '11', 'б': '12', 'в': '13', 'г': '14', 'д': '15', 'е': '16',
        'ж': '21', 'з': '22', 'и': '23', 'й': '24', 'к': '25', 'л': '26',
        'м': '31', 'н': '32', 'о': '33', 'п': '34', 'р': '35', 'с': '36',
        'т': '41', 'у': '42', 'ф': '43', 'х': '44', 'ц': '45', 'ч': '46',
        'ш': '51', 'щ': '52', 'ъ': '53', 'ы': '54', 'ь': '55', 'э': '56',
        'ю': '61', 'я': '62'
    }

    encrypted_text = ''.join(polybius_table.get(char, char) for char in text)
    return encrypted_text

def polybius_square_decipher(text: str) -> str:
    """Расшифровка квадрат Полибия."""
    polybius_table = {
        '11': 'а', '12': 'б', '13': 'в', '14': 'г', '15': 'д', '16': 'е',
        '21': 'ж', '22': 'з', '23': 'и', '24': 'й', '25': 'к', '26': 'л',
        '31': 'м', '32': 'н', '33': 'о', '34': 'п', '35': 'р', '36': 'с',
        '41': 'т', '42': 'у', '43': 'ф', '44': 'х', '45': 'ц', '46': 'ч',
        '51': 'ш', '52': 'щ', '53': 'ъ', '54': 'ы', '55': 'ь', '56': 'э',
        '61': 'ю', '62': 'я'
    }

    pairs = [text[i:i+2] for i in range(0, len(text), 2)]

    decrypted_text = ''.join(polybius_table.get(pair, pair) for pair in pairs)
    return decrypted_text
