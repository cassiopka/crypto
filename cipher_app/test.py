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
    for i in range(len(sequence)):
        result.append((list1[i] + sequence[i]) % 32)
    return result

def numeric_to_text(numeric_values):
    """Функция для преобразования числового эквивалента в текст."""
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    text = ''
    for value in numeric_values:
        if 1 <= value <= len(alphabet):
            text += alphabet[value - 1]
    return text

# User input

# Your list1
list1 = [5,  14, 12, 12, 14, 6,  8, 15, 18, 10, 1,  10, 2,  27, 12, 1,  11, 18, 27, 13, 9,  2,  27, 11, 8, 15, 18, 18, 27, 12, 13, 6,  10, 1,  7,  6, 24, 28, 17, 31, 1,  2,  2, 1,  18, 17, 18, 3,  14, 12, 18, 23, 10]  # Replace this with your list1

# Generate the sequence
sequence = linear_congruential_generator(a, c, t0)

# Process the list
processed_list = process_list(list1, sequence)

# Convert processed_list to text
processed_text = numeric_to_text(processed_list)

print("First 100 numbers in the sequence (without T(0)):", sequence)
print("Processed list:", processed_list)
print("Processed text:", processed_text)










