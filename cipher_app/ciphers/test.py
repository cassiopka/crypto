import numpy as np

def matrix_decipher(encrypted_message, key_matrix):
    """Дешифрование матричного шифра."""
    decrypted_messages = []
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    key_size = key_matrix.shape[0]
    split_message = [encrypted_message[i:i+2] for i in range(0, len(encrypted_message), 2)]
    
    vectors = []
    for i in range(0, len(split_message), key_size):
        vectors.append(split_message[i:i+key_size])
        
    encrypted_vectors = np.array(vectors, dtype=int)  

    
    inverse_key_matrix = np.linalg.inv(key_matrix)

    for vector in encrypted_vectors:
        decrypted_vector = np.dot(inverse_key_matrix, vector)
        decrypted_str = ''.join([str(int(round(x))) for x in decrypted_vector])
        decrypted_messages.append(decrypted_str)
    decrypted_text = ''
    for message in decrypted_messages:
        for num in message:
            if num != '':  
                letter_index = int(num) - 1  
                decrypted_text += alphabet[letter_index]
    return ''.join(decrypted_text)


encrypted_message = "283567212638"
key_matrix = np.array([[1, 4, 8], [3, 7, 2], [6, 9, 5]])
decrypted_text = matrix_decipher(encrypted_message, key_matrix)

print("Расшифрованный текст:")
print(decrypted_text)
