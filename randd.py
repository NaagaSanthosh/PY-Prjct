import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_letters=True, use_digits=True, use_special_chars=True):
        self.length = length
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars

    def generate_password(self):
        characters = ''
        if self.use_letters:
            characters += string.ascii_letters
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation

        if not characters:
            return "Error: No character set selected for the password."

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

# Example usage:
password_generator = PasswordGenerator(length=16, use_letters=True, use_digits=True, use_special_chars=True)
password = password_generator.generate_password()
print("Random Password:", password)
