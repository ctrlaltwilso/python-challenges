# ---- Array Hopping Challenges ---- #
# Challenge:
# Traverse through three arrays and record the max value from B & C
# Traversal order: A -> B -> A -> C
# Use the value of the list item to determine the next index
# Exaample: ArrayA[1] = 2 -> ArrayB[2]
# Repeat processs until:
    # repeat an index in B or C
    # Access an index > len(array)
# Return SUM(max value of B + C)

def solution(arrayA, arrayB, arrayC):
    arrays = [arrayA, arrayB, arrayA, arrayC]
    phase = 0 
    position = 0

    visited = set()

    maxB = float('-inf')
    maxC = float('-inf')

    while True:
        if (position, phase) in visited:
            return maxB + maxC
        else:
            if position >= len(arrays[phase]):
                return maxB + maxC
                
            if phase == 1 and maxB < arrays[phase][position]:
                maxB = arrays[phase][position]
            elif phase == 3 and maxC < arrays[phase][position]:
                maxC = arrays[phase][position]
                
            visited.add((position, phase))
            position = arrays[phase][position]
            phase = (phase + 1) % 4

# --- Test Cases --- #

arrayA = [2, 1, 3, 0]
arrayB = [1, 3, 2, 4]
arrayC = [4, 2, 5, 3]
assert solution(arrayA, arrayB, arrayC) == 7, "Failed Test 1"

arrayA = [2, 0, 1]
arrayB = [1, 3, 2]
arrayC = [2, 0, 1]
assert solution(arrayA, arrayB, arrayC) == 2, "Failed Test 2"

arrayA = [0, 2, 0]
arrayB = [1, 1, 2]
arrayC = [0, 1, 2]
assert solution(arrayA, arrayB, arrayC) == 3, "Failed Test 3"

arrayA = [1, 1, 2, 0]
arrayB = [2, 2, 1, 3]
arrayC = [1, 2, 3, 4]
assert solution(arrayA, arrayB, arrayC) == 5, "Failed Test 4"