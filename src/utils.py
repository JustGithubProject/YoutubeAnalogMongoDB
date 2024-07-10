import hashlib
import string
import random
import shutil
import os

from uuid import uuid4


def generate_string():
    letters = string.ascii_letters
    return "".join([random.choice(letters) for _ in range(20)])   


def generate_hash_based_on_string():
    generated_string = generate_string()
    return hashlib.sha256(generated_string.encode()).hexdigest()



def save_file(object_path, file_bytes):
    filename = f"{uuid4()}_{object_path.filename}"
    full_path = os.path.join("/app/uploads", filename)
    with open(full_path, "wb") as file:
        file.write(file_bytes)
    return full_path
         
    