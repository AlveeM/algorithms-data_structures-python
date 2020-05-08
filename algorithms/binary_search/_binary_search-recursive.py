def binary_search_recursive(array, target, start_idx, end_idx):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_idx > end_idx:
        return -1

    mid_idx = (start_idx + end_idx) // 2
    mid_el = array[mid_idx]

    if mid_el == target:
        return mid_idx
    elif target < mid_el:
        return binary_search_recursive(array, target, start_idx, mid_idx - 1)
    else:
        return binary_search_recursive(array, target, start_idx + 1, end_idx)
