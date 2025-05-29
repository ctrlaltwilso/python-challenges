# ---- Frequency Calculation  Challenges ---- #
# Challenge:
# input an array of integers, 1 to 100 inclusive
# For  each number that is not a multipple of 10, increase by 1
# For each number that is multiple of 10, assign value of 1
# Afterwards calculate the frequency of of each number
# return an array of (number * frequency) in ascending order

def solution(numbers):
    calc_nums = []

    for num in numbers:
        if num % 10 > 0:
            calc_nums.append(num + 1)
        else:
            calc_nums.append(1)

    calc_dict = {}
    for num in calc_nums:
        if num in calc_dict:
            calc_dict[num] += 1
        else:
            calc_dict[num] = 1

    final_output = []
    for num, frequency in calc_dict.items():
        final_output.append(num * frequency)

    final_output.sort()
    return final_output

print(solution([5, 10, 15, 10, 5, 15]))

# --- Test Cases --- #
input_data = [1, 2, 3, 4, 5]
expected_output = [2, 3, 4, 5, 6]
assert solution(input_data) == expected_output, "Failed Test 1"

input_data = [10, 20, 30, 40, 50]
expected_output = [5]
assert solution(input_data) == expected_output, "Failed Test 1"

input_data = [10]
expected_output = [1]
assert solution(input_data) == expected_output, "Failed Test 1"

input_data = [-100, -50, 0, 50, 100]
expected_output = [5]
assert solution(input_data) == expected_output, "Failed Test 1"