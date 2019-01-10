# we want to divide and conquer our sorting
# O(n log n)
import time

def merge_sort(array, debug=False):
    start = time.time()

    sorted_array = _merge_sort(array, debug)

    end = time.time()

    if debug:
        print("""
        Summary: Merge Sort
        Start: {}
        End: {}
        Duration: {}
        """.format(start, end, end - start))

    return sorted_array

def _merge_sort(array, debug=False):
    if len(array) == 1:
        if debug:
            print(array)

        return array

    mid_point = int(len(array) / 2)

    left = _merge_sort(array[:mid_point], debug)
    right = _merge_sort(array[mid_point:], debug)
    
    left_pointer = 0
    right_pointer = 0
    sorted_array = []
    
    while left_pointer < len(left) and right_pointer < len(right):
        left_value = left[left_pointer]
        right_value = right[right_pointer]

        if left_value < right_value:
            sorted_array.append(left_value)
            left_pointer += 1
        elif left_value > right_value:
            sorted_array.append(right_value)
            right_pointer += 1
        else:
            sorted_array.append(left_value)
            left_pointer += 1
            sorted_array.append(right_value)
            right_pointer += 1
            
    if left_pointer < len(left):
        sorted_array += left[left_pointer:]
    elif right_pointer < len(right):
        sorted_array += right[right_pointer:]

    if debug:
        print(sorted_array)

    return sorted_array

    