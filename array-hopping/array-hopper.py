# ---- Array Hopping ---- #
# Challenge: 
# Function with two input arrays
# Traverse both arrays by using the value of the array
# Example: arrayA[0] = 2 -> arrayB[2]
# Hop arrays until a character lands on an index in arrayA that has already visited.
# return all values that it traveled

def solution(arrayA, arrayB):
    final_output = []
    visited = []
    indexA = 0
    indexB = None

    while True:
        if indexA not in visited:
                indexB = arrayA[indexA] - 1
                final_output.append(indexB + 1)
                visited.append(indexA)
                indexA = arrayB[indexB] - 1
        else:
            return final_output
            
        

arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4,  3,  2,  1]

print(solution(arrayA, arrayB))


# --- Test Cases --- #
arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4, 3, 2, 1]
expected_output = [1, 4, 3, 2, 5]
assert solution(arrayA, arrayB) == expected_output, "Failed Test 1"

arrayA = [1, 1, 1, 1, 1]
arrayB = [1, 2, 3, 4, 5]
expected_output = [1]
assert solution(arrayA, arrayB) == expected_output, "Failed Test 2"

arrayA = [2, 3, 4, 5, 1]
arrayB = [5, 4, 3, 2, 1]
expected_output = [2, 5]
assert solution(arrayA, arrayB) == expected_output, "Failed Test 3"

arrayA = [1, 5, 2, 4, 3]
arrayB = [1, 2, 3, 4, 5]
expected_output = [1]
assert solution(arrayA, arrayB) == expected_output, "Failed Test 4"