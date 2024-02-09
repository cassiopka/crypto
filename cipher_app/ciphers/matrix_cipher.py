import numpy as np

def matrix_cipher(text_numeric, key_matrix):
    """Матричный шифр."""
    encrypted_messages = []
    key_size = key_matrix.shape[0]

    # Подготовка текста к шифрованию: разбиение на векторы длиной key_size
    text_chunks = [text_numeric[i:i+key_size] for i in range(0, len(text_numeric), key_size)]

    # Шифрование каждого вектора текста
    for chunk in text_chunks:
        # Дополнение вектора нулями до длины key_size, если необходимо
        while len(chunk) < key_size:
            chunk.append(0)
        # Умножение ключевой матрицы на вектор текста
        encrypted_vector = np.dot(key_matrix, chunk)
        # Добавление зашифрованного вектора в список зашифрованных сообщений
        encrypted_messages.append(encrypted_vector)

    # Конвертация списка зашифрованных сообщений в строку
    encrypted_str = ' '.join([str(vector) for vector in encrypted_messages]).replace('[', '').replace(']', '').replace(' ', '')
    return encrypted_str

def matrix_decipher(encrypted_message, key_matrix):
    """Дешифрование матричного шифра."""
    decrypted_messages = []
    key_size = key_matrix.shape[0]

    # Получение числового представления зашифрованного сообщения
    encrypted_vectors = [np.array(list(map(int, encrypted_message[i:i+key_size]))) for i in range(0, len(encrypted_message), key_size)]

    # Вычисление обратной матрицы ключа
    inverse_key_matrix = np.linalg.inv(key_matrix)

    # Дешифрование каждого вектора текста
    for vector in encrypted_vectors:
        # Умножение обратной ключевой матрицы на вектор зашифрованного текста
        decrypted_vector = np.dot(inverse_key_matrix, vector)
        # Преобразование дешифрованного вектора в строку чисел без пробелов и знаков
        decrypted_str = ''.join([str(int(x)) for x in decrypted_vector])
        # Добавление дешифрованного сообщения в список дешифрованных сообщений
        decrypted_messages.append(decrypted_str)

    # Объединение всех дешифрованных сообщений в одну строку
    return ''.join(decrypted_messages)
