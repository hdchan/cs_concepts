# we find the lowest value and put it in it's place
# O(n^2) time complexity
import copy
import time

def selection_sort(array, debug=False):
    copy_array = copy.deepcopy(array)
    iter_count = 0
    start = time.time()

    for idx, element in enumerate(copy_array):
        lowest_value = element
        lowest_value_index = idx
        for inner_idx in range(idx, len(copy_array)):
            current_value = copy_array[inner_idx]
            
            if current_value < lowest_value:
                lowest_value = current_value
                lowest_value_index = inner_idx
            
            if debug:
                print("Iteration {}: {}".format(iter_count, copy_array))

            iter_count += 1
        
        copy_array[idx] = copy_array[lowest_value_index]
        copy_array[lowest_value_index] = element
        
    end = time.time()

    if debug:
        print("""
        Summary: Selection Sort
        Start: {}
        End: {}
        Duration: {}
        Iteration Count: {}
        """.format(start, end, end - start, iter_count))

    return copy_array