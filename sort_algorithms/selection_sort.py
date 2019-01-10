# we find the lowest value and put it in it's place
# O(n^2) time complexity
import time

def selection_sort(array, debug=False, verbose=False):
    iter_count = 0
    start = time.time()

    for idx, element in enumerate(array):
        lowest_value = element
        lowest_value_index = idx
        for inner_idx in range(idx, len(array)):
            current_value = array[inner_idx]
            
            if current_value < lowest_value:
                lowest_value = current_value
                lowest_value_index = inner_idx
            
            if debug and verbose:
                print("Iteration {}: {}".format(iter_count, array))

            iter_count += 1
        
        array[idx] = array[lowest_value_index]
        array[lowest_value_index] = element
        
    end = time.time()

    if debug:
        print("""
        Summary: Selection Sort
        Start: {}
        End: {}
        Duration: {}
        Iteration Count: {}
        """.format(start, end, end - start, iter_count))

    return array