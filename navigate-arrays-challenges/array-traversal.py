# ---- Navigating Arrays Challenges ---- #
# Challenge:
# Given a list of arrays, each value represents an index look ahead
# If in the lookhead distance there is an obstacle(a negative integer)
    #return the index of the negative integer
# if there is not an obstacle, return the original number
# obstacles return as -1

# Example: 
# Input: [3, 2, -3, 1, 2]
# Output: [2, 2, -1, 1, 2]

def solution(numbers):
    position = 0
    final_output = []

    while position < len(numbers):
        if numbers[position] < 0:
            final_output.append(-1)
        else:
            found_obstacle = False
            for i in range(position + 1, min(position + numbers[position] + 1, len(numbers))):
                if numbers[i] < 0:
                    final_output.append(i)
                    found_obstacle = True
                    break
            if not found_obstacle:
                final_output.append(numbers[position])
        position += 1

    return final_output

num = [3, 2, -3, 1, 2]
print(solution(num))

# --- Test Cases --- #
assert solution([-1, 2, 3, 4, 5]) == [-1, 2, 3, 4, 5], "Failed Test 1"
assert solution([5, 4, 3, 2, 1, -1]) == [5, 5, 5, 5, 5, -1], "Failed Test 2"
assert solution([7, 6, 5, 4, -1, 2, 1]) == [4, 4, 4, 4, -1, 2, 1], "Failed Test 3"
assert solution([1, 1, 1, 1, 1, 1, -1]) == [1, 1, 1, 1, 1, 6, -1], "Failed Test 4"