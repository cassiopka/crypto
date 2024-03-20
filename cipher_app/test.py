from utils.input_formatter import format_input
import math

def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q = b // a
        b, a, u, v = a, b % a, v, u - q * v
        x, y = y, x - q * y
    return b, x, y

def modular_inverse(e, fi):
    gcd, x, y = extended_gcd(e, fi)
    if gcd != 1:
        raise ValueError("e и fi не являются взаимно простыми")
    return x % fi


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_position(letter, alphabet):
    return alphabet.index(letter)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_keys():
    while True:
        p = int(input("Введите простое число p (> 2): "))
        if is_prime(p) and p > 2:
            break
        else:
            print("Число p должно быть простым и больше 2. Попробуйте еще раз.")

    while True:
        q = int(input("Введите простое число q (> 2): "))
        if is_prime(q) and q > 2 and q != p:
            break
        else:
            print("Число q должно быть простым, больше 2 и не равно p. Попробуйте еще раз.")

    n = p * q
    fi = (p - 1) * (q - 1)

    allowed_e_values = []
    for i in range(2, fi):
        if gcd(i, fi) == 1:
            allowed_e_values.append(i)

    while True:
        e = int(input("Введите число e, взаимно простое с fi (пример допустимых значений: {}): ".format(allowed_e_values)))
        if e in allowed_e_values:
            break
        else:
            print("Число e должно быть одним из допустимых значений. Попробуйте еще раз.")

    # ed ≡ 1 (mod fi)
    # То есть, мы ищем число d, которое является мультипликативным обратным к числу e по модулю fi
    # d = (1 + k * fi) / e
    # где k - целое число, такое что (1 + k * fi) делится на e.
    # для k используем расширенным алгоритмом Евклида
    d = modular_inverse(e, fi)
    return (e, n), (d, n)



def encrypt(text, key):
    e, n = key
    encrypted_text = []
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    for char in text:
        if char not in alphabet:
            print("Недопустимый символ в тексте. Допускаются только строчные буквы русского алфавита.")
            return None
        position = find_position(char, alphabet) + 1
        encrypted_position = pow(position, e, n)
        encrypted_text.append(encrypted_position)
    return encrypted_text


def decrypt(encrypted_text, key):
    d, n = key
    decrypted_text = []
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    for position in encrypted_text:
        decrypted_position = pow(position, d, n)
        decrypted_char = alphabet[decrypted_position - 1]
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

if __name__ == "__main__":
    print("Шифрование и дешифрование RSA")
    public_key, private_key = generate_keys()
    text = input("Введите текст для шифрования: ")
    encrypted_text = encrypt(format_input(text), public_key)
    if encrypted_text is not None:
        print("Зашифрованный текст:", encrypted_text)
        decrypted_text = decrypt(encrypted_text, private_key)
        print("Дешифрованный текст:", decrypted_text)