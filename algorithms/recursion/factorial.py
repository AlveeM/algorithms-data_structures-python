def factorial_iter(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

print(factorial_iter(4))

def dispatcher(n):
    if n == 0:
        return 1

    result = n * factorial_iter(n - 1)
    return result

print(dispatcher(4))

def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1

    result = n * factorial(n-1)
    return result

print(factorial(4))

# Test Cases

print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")