def is_palindrome_iter(input):
    midpoint = len(input) // 2
    palindrome = True

    for i in range(midpoint):
        left_char = input[i]
        right_char = input[len(input)-i-1]
        if left_char != right_char:
            palindrome = False
            break

    return palindrome

def dispatch(input):
    if len(input) <= 1:
        return True

    first_char = input[0]
    last_char = input[-1]

    substring = input[1:-1]

    return (first_char == last_char) and is_palindrome_iter(substring)

def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) <= 1:
        return True

    first_char = input[0]
    last_char = input[-1]
    substring = input[1:-1]

    return (first_char == last_char) and is_palindrome(substring)

# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
