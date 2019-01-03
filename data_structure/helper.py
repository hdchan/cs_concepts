from data_structure.stack import Stack
from data_structure.stack_double_link import StackDoubleLink
from data_structure.linked_list_double import LinkedListDouble
import random

# Helper function
def generate_randomized_linked_list(value_range=9, stack_size=10):
    linked_list = LinkedListDouble()
    for i in range(stack_size):
        random_int = random.randint(0, value_range)
        linked_list.append(random_int)
    return linked_list

def generate_randomized_stack(value_range=9, stack_size=10):
    stack = Stack()
    for i in range(stack_size):
        random_int = random.randint(0, value_range)
        stack.push(random_int)
    return stack

def generate_randomized_stack_double_link(value_range=9, stack_size=10):
    stack = StackDoubleLink()
    for i in range(stack_size):
        random_int = random.randint(0, value_range)
        stack.push(random_int)
    return stack