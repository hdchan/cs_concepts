# we constantly loop through each element and swapping values
# using indicator to determine if we've finished swapping
# O(n^2) time complexity
import time

def bubble_sort(array, debug=False, verbose=False):
    iter_count = 0
    start = time.time()
    
    did_sort = True

    while did_sort == True:
        did_sort = False

        for idx, current_element in enumerate(array):
            if (idx + 1 == len(array)):
                continue
            next_element = array[idx + 1]
            if current_element > next_element:
                temp = current_element
                array[idx] = next_element
                array[idx + 1] = temp
                did_sort = True
                if debug and verbose:
                    print("Iteration {}: {} -- swapped {} and {}".format(iter_count, array, current_element, next_element))
            else:
                if debug and verbose:
                    print("Iteration {}: {} -- nothing to swap".format(iter_count, array))
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

    # return copy_array