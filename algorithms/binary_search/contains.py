def contains(target, source):
    if len(source) == 0:
        return False

    mid_idx = (len(source) - 1) // 2

    if source[mid_idx] == target:
        return True
    elif source[mid_idx] > target:
        return contains(target, source[ :mid_idx])
    else:
        return contains(target, source[mid_idx + 1:])

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False