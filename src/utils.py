import hashlib
import string
import random
import shutil
import os


def generate_string():
    letters = string.ascii_letters
    return "".join([random.choice(letters) for _ in range(20)])   


def generate_hash_based_on_string():
    generated_string = generate_string()
    return hashlib.sha256(generated_string.encode()).hexdigest()


def save_file(file_location: str, video_path):
    root_directory = os.path.abspath(".")
    path_to_file = os.path.join(root_directory, "src", file_location)
    with open(path_to_file, "wb+") as file:
        shutil.copyfileobj(video_path.file, file)
    return path_to_file