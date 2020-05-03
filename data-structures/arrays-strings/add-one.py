def add_one(arr):
    carry = 1

    for i in range(len(arr)-1, -1, -1):
        digit = carry + arr[i]
        carry = digit // 10

        if carry == 0:
            arr[i] = digit
            break
        else:
            arr[i] = 0

    new_arr = [carry] + arr
    split_idx = 0
    while new_arr[split_idx] == 0:
        split_idx += 1

    return new_arr[split_idx:]

# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)