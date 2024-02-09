import numpy as np

def matrix_decipher(encrypted_message, key_matrix):
    """Дешифрование матричного шифра."""
    decrypted_messages = []
    key_size = key_matrix.shape[0]
    message_chunks = [encrypted_message[i:i+2] for i in range(0, len(encrypted_message), 2)]
    encrypted_vectors = [np.array(list(map(int, chunk))) for chunk in message_chunks]


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

# Пример использования функции для дешифровки
encrypted_message = "283567212638"
key_matrix = np.array([[1, 4, 8], [3, 7, 2], [6, 9, 5]])
decrypted_message = matrix_decipher(encrypted_message, key_matrix)
print("Дешифрованное сообщение:")
print(decrypted_message)
