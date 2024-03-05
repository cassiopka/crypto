class VerticalPermutation:
    key_string = "аб"
    example_alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')

    def __init__(self, key):
        self.key = key

    @staticmethod
    def key_to_int(key_string):
        positions = [-1] * len(key_string)
        for i, char in enumerate(key_string):
            if char in VerticalPermutation.example_alphabet:
                positions[i] = VerticalPermutation.example_alphabet.index(char)

        for j in range(len(positions)):
            min_val = len(VerticalPermutation.example_alphabet) + 1
            for i, position in enumerate(positions):
                if 0 <= position < min_val:
                    min_val = position
            min_index = positions.index(min_val)
            positions[min_index] = -(j + 1)

        result = ''.join(str(-p) for p in positions if p < 0)
        return result

    def get_encrypted(self, text):
        self.prepare_to_crypt(text)
        return self.encrypt()

    def get_decrypted(self, text):
        self.prepare_to_crypt(text)
        return self.decrypt()

    def prepare_to_crypt(self, text):
        self.text = text.replace(" ", "").upper()
        self.text += " " * (len(self.text) % len(self.key_string))
        self.chars_i = len(self.text) // len(self.key)
        self.chars_j = len(self.key)

    def encrypt(self):
        result = []
        chars = self.string_to_char_arr(self.text, True, self.chars_i, self.chars_j)
        for j in range(self.chars_j):
            for i in range(self.chars_i):
                result.append(chars[i][int(self.key[j]) - 1])
            result.append(" ")
        return ''.join(result)

    def decrypt(self):
        result = []
        chars = self.string_to_char_arr(self.text, False, self.chars_i, self.chars_j)
        for i in range(self.chars_i):
            for j in range(self.chars_j):
                result.append(chars[i][self.key.index(str(j + 1))])
        return ''.join(result)

    @staticmethod
    def string_to_char_arr(string, by_line, chars_i, chars_j):
        chars = [[''] * chars_j for _ in range(chars_i)]
        if by_line:
            for i in range(chars_i):
                for j in range(chars_j):
                    chars[i][j] = string[i * chars_j + j]
        else:
            for j in range(chars_j):
                for i in range(chars_i):
                    chars[i][j] = string[j * chars_i + i]
        return chars