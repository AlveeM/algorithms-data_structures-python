def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] < number:
            start = mid + 1
        elif arr[mid] > number:
            end = mid - 1
        else:
            return [find_first(arr, number, 0, mid),
                    find_last(arr, number, mid, len(arr) - 1)]

    return [-1, -1]


def find_first(arr, number, start, end):
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < number:
            start = mid + 1
        elif arr[mid-1] < number:
            return mid
        else:
            end = mid - 1
    return start


def find_last(arr, number, start, end):
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > number:
            end = mid - 1
        elif arr[mid+1] > number:
            return mid
        else:
            start = mid + 1
    return end


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)