import hashlib
import string
import random


def generate_string():
    letters = string.ascii_letters
    return "".join([random.choice(letters) for _ in range(20)])   


def generate_hash_based_on_string():
    generated_string = generate_string()
    return hashlib.sha256(generated_string.encode()).hexdigest()