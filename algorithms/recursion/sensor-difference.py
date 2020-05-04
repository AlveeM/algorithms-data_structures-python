# iterative solution
def total_diff(sensorA, sensorB, size):
    diff = 0
    for i in range(size):
        diff += abs(sensorA[i] - sensorB[i])

    return diff


first_sensor = [15, -4, 56, 10, -23]
second_sensor = [14, -9, 56, 14, -23]
sensor_size = len(first_sensor)

print(total_diff(first_sensor, second_sensor, sensor_size)) # 10


# Dispatcher does two things
# 1. Solves the problem for some "minimal" data set
    # In this case, when size == 0
# 2. Calls iterative function to handle non-minimal cases
    # IMPORTANT: must pass smaller data set to iterative function
    # In this case, passing (size - 1) for third parameter
    # Dispatcher must then handle last elements in the arrays
def dispatcher(sensorA, sensorB, size):
    if size == 0:
        return 0

    last_element_diff = abs(sensorA[size - 1] - sensorB[size - 1])
    diff = total_diff(sensorA, sensorB, size - 1) + last_element_diff
    return diff

print(dispatcher(first_sensor, second_sensor, sensor_size))


# Recursive Solution
# change the call to the iterative function in the dispatcher to itself
def diff_recursive(sensorA, sensorB, size):
    if size == 0:
        return 0

    last_element_diff = abs(sensorA[size - 1] - sensorB[size - 1])
    diff = diff_recursive(sensorA, sensorB, size - 1) + last_element_diff
    return diff

print(diff_recursive(first_sensor, second_sensor, sensor_size))
