# Name: Brendan Cahill
# OSU Email: cahillbr@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: 1
# Due Date: 1/30/23
# Description: introduction to python assignments with array


import random
from static_array import *



# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    minimum = arr.get(0)  #assigning values of arraw both min and max
    maximum = arr.get(0)
    for i in range(arr.length()):
        if arr.get(i) < minimum: # scenarios for values if either is less than or grater than min or max value
            minimum = arr.get(i)
        elif arr.get(i) > maximum:
            maximum = arr.get(i)
    return (minimum, maximum)


pass

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    new_arr = StaticArray(arr.length())
    for i in range(arr.length()):
        if arr.get(i) % 3 == 0 and arr.get(i) % 5 == 0: # conditionals on which value is divisble by 3 or 5
            new_arr.set(i, "fizzbuzz")  # also with conditional if 3 or 5 are multiples
        elif arr.get(i) % 5 == 0:
            new_arr.set(i, "buzz")
        elif arr.get(i) % 3 == 0:
            new_arr.set(i, "fizz")
        else:
            new_arr.set(i, arr.get(i))
    return new_arr

    pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    for index in range(arr.length() // 2):  #reverse order of elements in array
        temp = arr.get(index)
        arr.set(index, arr.get(arr.length() - 1 - index))
        arr.set(arr.length() - 1 - index, temp)
    pass

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    set_arr = StaticArray(arr.length()) # function receievs the given paramters of shifting for direction
    for i in range(arr.length()):  # right = positive and vice versa
        new_index = (i + steps) % arr.length()
        set_arr.set(new_index, arr.get(i))
    return set_arr

    pass

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    arr = StaticArray(end - start + 1)
    for i, j in enumerate(range(start, end + 1)):
        arr.set(i, k)
    return arr

    pass

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    descending = True
    ascending = True
    for i in range(1, arr.length()):
        if arr.get(i) < arr.get(i - 1):
            ascending = False
        if arr.get(i) > arr.get(i - 1):
            descending = False
        if not ascending and not descending:
            return 0
    return 1 if ascending else -1
    pass

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    max_count = 1
    current_count = 1
    mode = arr.get(0)
    for i in range(1, arr.length()):
        if arr.get(i) == arr.get(i - 1):
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                mode = arr.get(i)
        else:
            current_count = 1
    return (mode, max_count)
    pass

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    unique = StaticArray(1)
    unique.set(0, arr.get(0))
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            unique.set(unique.length(), arr.get(i))
    return unique
    pass

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    max_value = arr.get(0)
    for i in range(1, arr.length()):
        if arr.get(i) > max_value:
            max_value = arr.get(i)
    count = [0] * (max_value + 1)
    for i in range(arr.length()):
        count[arr.get(i)] += 1
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]
    sorted_array = StaticArray(arr.length())
    for i in range(arr.length() - 1, -1, -1):
        sorted_array.set(count[arr.get(i)] - 1, arr.get(i))
        count[arr.get(i)] -= 1
    return sorted_array

    pass

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    squares = StaticArray(arr.length())
    l, r = 0, arr.length() - 1
    for i in range(arr.length() - 1, -1, -1):
        if abs(arr.get(l)) > abs(arr.get(r)):
            squares.set(i, arr.get(l)**2)
            l += 1
        else:
            squares.set(i, arr.get(r)**2)
            r -= 1
    return squares
    pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
