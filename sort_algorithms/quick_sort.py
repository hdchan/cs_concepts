# Another O(n log n) sorting mechanism
# We sort by picking a pivot point to compare against
import time
import random

# randomly picks a value to pivot
def quick_sort_naive(array, debug=False):
    start = time.time()

    sorted_array = _quick_sort_naive(array, debug)

    end = time.time()

    if debug:
        print("""
        Summary: Quick Sort Naive
        Start: {}
        End: {}
        Duration: {}
        """.format(start, end, end - start))

    return sorted_array    

def _quick_sort_naive(array, debug=False):
    if len(array) <= 1:
        if debug and len(array) == 1:
            print(array)

        return array

    pivot_index = random.randint(0, len(array) - 1)
    pivot_value = array[pivot_index]
    
    if debug:
        print("Picked pivot {} at index {} from {}".format(pivot_value, pivot_index, array))

    low = []
    equal = []
    high = []

    for i in array:
        if i < pivot_value:
            low.append(i)
        elif i > pivot_value:
            high.append(i)
        elif i == pivot_value:
            equal.append(i)

    merged = _quick_sort_naive(low, debug) + _quick_sort_naive(equal, debug) + _quick_sort_naive(high, debug)

    if debug:
        print(merged)

    return merged

#######################################

# picking last value in array
def quick_sort_lomuto(array, debug=False):
    start = time.time()

    _quick_sort_lomuto(array, 0, len(array) - 1, debug)

    end = time.time()

    if debug:
        print("""
        Summary: Quick Sort Lomuto
        Start: {}
        End: {}
        Duration: {}
        """.format(start, end, end - start))


def _quick_sort_lomuto(array, low, high, debug=False):
    if low < high:
        pivot_index = _partition_lomuto(array, low, high, debug)
        _quick_sort_lomuto(array, low, pivot_index - 1, debug)
        _quick_sort_lomuto(array, pivot_index + 1, high, debug)

def _partition_lomuto(array, low, high, debug=False):
    
    pivot = array[high]
    pivot_index = 0

    for i in range(pivot_index, high):
        current_value = array[i]
        if current_value <= pivot:
            array[i] = array[pivot_index]
            array[pivot_index] = current_value
            pivot_index += 1
    
    array[high] = array[pivot_index]
    array[pivot_index] = pivot
    
    return pivot_index


#######################################

def quick_sort_median(array, debug=False):
    start = time.time()

    _quick_sort_median(array, 0, len(array) - 1, debug)

    end = time.time()

    if debug:
        print("""
        Summary: Quick Sort Median
        Start: {}
        End: {}
        Duration: {}
        """.format(start, end, end - start))

def _quick_sort_median(array, low, high, debug=False):
    if low < high:
        # sort low, middle and high
        center_index = _median_of_three(array, low, high, debug)
        # swap middle and high
        center_value = array[center_index]
        array[center_index] = array[high]
        array[high] = center_value
        # call lomuto sort
        pivot_index = _partition_lomuto(array, low, high, debug)
        _quick_sort_lomuto(array, low, pivot_index - 1, debug)
        _quick_sort_lomuto(array, pivot_index + 1, high, debug)

def _median_of_three(array, low, high, debug=False):
    # return median value of three values
    if debug:
        print("Array before median swap {}".format(array))
    center = int((low + high) / 2)
    if array[low] > array[center]:
        temp_value = array[center]
        array[center] = array[low]
        array[low] = temp_value
    if array[low] > array[high]:
        temp_value = array[high]
        array[high] = array[low]
        array[low] = temp_value
    if array[center] > array[high]:
        temp_value = array[high]
        array[high] = array[center]
        array[center] = temp_value
    if debug:
        print("Array before median swap {}".format(array))
    return center