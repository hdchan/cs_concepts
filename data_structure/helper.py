from data_structure.stack import Stack
import random

# Helper function
def generate_randomized_stack(value_range=9, stack_size=10):
    stack = Stack()
    for i in range(stack_size):
        random_int = random.randint(0, value_range)
        stack.push(random_int)
    return stack