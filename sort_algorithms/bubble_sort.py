# we constantly loop through each element and swapping values
# using indicator to determine if we've finished swapping
# O(n^2) time complexity
import copy
import time

def bubble_sort(array, debug=False):
    iter_count = 0
    start = time.time()
    did_sort = True
    copy_array = copy.deepcopy(array)
    while did_sort == True:
        did_sort = False
        for idx, current_element in enumerate(copy_array):
            if (idx + 1 == len(copy_array)):
                continue
            next_element = copy_array[idx + 1]
            if current_element > next_element:
                temp = current_element
                copy_array[idx] = next_element
                copy_array[idx + 1] = temp
                did_sort = True
                if debug:
                    print("Iteration {}: {} -- swapped {} and {}".format(iter_count, copy_array, current_element, next_element))
            else:
                if debug:
                    print("Iteration {}: {} -- nothing to swap".format(iter_count, copy_array))
            iter_count += 1
    end = time.time()

    if debug == True:
        print("""
        Summary: Bubble Sort
        Start: {}
        End: {}
        Duration: {}
        Iteration Count: {}
        """.format(start, end, end - start, iter_count))
    print(debug)
    return copy_array