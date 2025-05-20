# ---- Nested Loop Challenges ---- #
# Problem: 
# Function that accepts two arrays of integers
# paired integers where sum of two elements is a perfect square
# order by the input of the first array
# if no pairs are found, return empty list
import math 

def find_sum_square(arr1, arr2):
    matches = []

    for n in arr1:
        for k in arr2:
            if (n + k) >= 0 and math.sqrt(n + k).is_integer():
                matches.append((n, k))

    return matches

arr1 = [2, 3, 16]
arr2 = [1, 9, 10]
print(find_sum_square(arr1, arr2))

# --- Test Cases --- #
arr1 = [2, 3, 16]
arr2 = [1, 9, 10]
expected = [(3,1), (16, 9)]
assert find_sum_square(arr1, arr2) == expected, "Failed Test 1"

arr1 = [4, 13, 23]
arr2 = [-4, -3, -25]
expected = [(4, -4), (4, -3), (13, -4)]
assert find_sum_square(arr1, arr2) == expected, "Failed Test 2"

arr1 = [100, 75, 36, 9, -25, -64, -100]
arr2 = [-1, 1, 24, 0, -1, -24]
expected = [(100, 0), (36, 0), (9, 0)]
assert find_sum_square(arr1, arr2) == expected, "Failed Test 3"

arr1 = []
arr2 = [1, 2, 3, 4]
expected = []
assert find_sum_square(arr1, arr2) == expected, "Failed Test 4"