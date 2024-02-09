def text_to_numeric(text):
    """Функция для преобразования текста в числовой эквивалент."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    numeric_values = []
    for char in text:
        if char.lower() in alphabet:
            numeric_value = alphabet.index(char.lower()) + 1
            numeric_values.append(numeric_value)
    return numeric_values
