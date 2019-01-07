# we want to divide and conquer our sorting
# O(n log n)
import copy
import time

def merge_sort(array, debug=False):
    copy_array = copy.deepcopy(array)
    start = time.time()

    copy_array = _merge_sort(copy_array)

    end = time.time()

    if debug:
        print("""
        Summary: Merge Sort
        Start: {}
        End: {}
        Duration: {}
        """.format(start, end, end - start))

    return copy_array

def _merge_sort(array):
    if len(array) == 1:
        print(array)
        return array

    mid_point = int(len(array) / 2)

    left = _merge_sort(array[:mid_point])
    right = _merge_sort(array[mid_point:])
    
    left_pointer = 0
    right_pointer = 0
    sorted_array = []
    

    for idx in range(0, (len(left) + len(right))):
        left_value = None
        right_value = None

        if left_pointer < len(left):
            left_value = left[left_pointer]
        if right_pointer < len(right):
            right_value = right[right_pointer]
            
        if right_value != None and left_value != None:
            if left_value < right_value:
                sorted_array.append(left_value)
                left_pointer += 1
            else: 
                sorted_array.append(right_value)
                right_pointer += 1
        elif right_value == None:
            sorted_array.append(left_value)
            left_pointer += 1
        else:
            sorted_array.append(right_value)
            right_pointer += 1
            
    print(sorted_array)
    return sorted_array

    