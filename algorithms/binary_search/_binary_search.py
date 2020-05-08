def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_idx = 0
    end_idx = len(array) - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        mid_el = array[mid_idx]

        if target == mid_el:
            return mid_idx
        elif target < mid_el:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1

    return -1
