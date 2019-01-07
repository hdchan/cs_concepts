import random

def generate_random_array(size=10):
    array = list(range(0, size))
    random.shuffle(array)
    return array
