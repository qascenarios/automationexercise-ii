

import random
import string
import json

def generate_random_email():
    return f"tester_{random.randint(10,999)}@mail.com"


def read_json(file_path):
    file = open(file_path, 'r')
    return json.load(file)


