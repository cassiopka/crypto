def linear_congruential_generator(a, c, t0, modulo=32):
    if a % 4 != 1:
        raise ValueError("a must be equal to 1 modulo 4")
    if c % 2 == 0:
        raise ValueError("c must be an odd number")

    sequence = []
    i = 0
    t_current = t0
    while i < 100:
        i += 1
        t_next = (a * t_current + c) % modulo
        sequence.append(t_next)
        if i > 1 and sequence[-1] in sequence[:-1]:
            break
        t_current = t_next

    return sequence

def process_list(list1, sequence):
    result = []
    i = 0
    while i < len(list1):
        result.append((list1[i] + sequence[i % len(sequence)]) % 32)
        i += 1
    return result

def numeric_to_text(numeric_values):
    """Функция для преобразования числового эквивалента в текст."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    text = ''
    for value in numeric_values:
        if 1 <= value <= len(alphabet):
            text += alphabet[value - 1]
    return text



def decrypt_text(numeric_values, sequence):
    result = []
    for i in range(len(sequence)):
        result.append((numeric_values[i] - sequence[i]) % 32)
    return result
