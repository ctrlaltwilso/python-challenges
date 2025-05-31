# ---- Navigating with Variables Challenge 002 ---- #
# Challenge
# Discover rotation of array 1 with min Manhatten distance w/ array 2
# return smallest possible Manhattan distance
# size of both arrays are always the same
# if  array1 = array2, return 0
# example
# array1 = [1,2,3]
# array2 = [2,2,4]
# Manhattan calculation = ∣1−2∣+∣2−2∣+∣3−4∣=1+0+1=2
    # calculate absolute values
# if calculation = best calculate
    # add numbers and assign best calculation to lowest numbers
    # example: array1 becomes 123

def solution(array1, array2):
    best_value = float('inf')
    best_rotation = None

    for k in range(len(array1)):
        rotated = array1[k:] + array1[:k]
        val = sum(abs(rotated[i] - array2[i]) for i in range(len(rotated)))

        if val < best_value:
            best_value, best_rotation = val, rotated
        elif val == best_value:
            if ''.join(str(x) for x in rotated) < ''.join(str(x) for x in best_rotation):
                best_rotation = rotated

    return best_rotation, best_value

# --- Test Cases --- #
assert solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == ([3, 4, 5, 1, 2], 6), "Failed Test 1"
assert solution([1, 2], [2, 1]) == ([2, 1], 0), "Failed Test 2"
assert solution([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == ([1, 2, 3, 4, 5], 0), "Failed Test 3"
assert solution([1, 2, 3], [2, 3, 1]) == ([2, 3, 1], 0), "Failed Test 4"