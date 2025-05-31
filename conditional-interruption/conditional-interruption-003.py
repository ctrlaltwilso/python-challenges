# ---- Conditional Interruption Challenges ---- #
# Challenge:
# Function inputs: Array of integers, String
# Subtract 3 from each absolute value of each number
    # If total >= 30, stop the process
# String -> if  lowercase
    # shift letters by 1 (a -> b)
    # else: leave as is

def solution(array, string):
    total = 0
    result = ''
    i = 0

    while i < len(array) and i < len(array):
        next_val = abs(array[i] - 3)
        if total + next_val > 30:
            break
        total += next_val
        if string[i].islower():
            result += chr((ord(string[i]) - ord('a') + 1) % 26 + ord('a'))
        else:
            result += string[i]
        i += 1

    return result, array[i:]

array = [5, 10, 15, 20, 25]
string = 'hello planet'
print(solution(array, string))

# --- Test Cases --- #
array = [-5, -10, -15, -20, -25]
string = "python is fun"
expected_output = ("qz", [-15, -20, -25])
assert solution(array, string) == expected_output, "Failed Test 1"

array = [10, 20, -10, -20, 30]
string = "coding mastery"
expected_output = ("dp", [-10, -20, 30])
assert solution(array, string) == expected_output, "Failed Test 2"

array = [11, 23, 32, -65, -33]
string = "buffalo buffalo buffalo"
expected_output = ("cv", [32, -65, -33])
assert solution(array, string) == expected_output, "Failed Test 3"

array = [40, -20, -10, -1, 1]
string = "race car"
expected_output = ("", [40, -20, -10, -1, 1])
assert solution(array, string) == expected_output, "Failed Test 4"
