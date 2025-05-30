# ---- Conditional Interruption Challenges ---- #
# Challenge:
# given a string of lowercase alphabetical characters
# calculate the absolute value of each number and multiply by 2
# accumulate results until the total exceeds 100
# for the string, replace ach letter with the preceding character
# Concat each char in order they were processed 
# vowels should not be processed, and stop the process
# 'y' is not considered a vowel
# return transformed string and remainder of the array in original order.

def solution(strings, numbers):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    total = 0
    result = ''
    i = 0

    while i < len(strings) and total <= 100 and strings[i] not in vowels:
        result += 'z' if strings[i] == 'a' else chr(ord(strings[i]) - 1)
        total += abs(numbers[i]) * 2
        i += 1
    
    return result, numbers[i:]


strings = 'xyzabc'
numbers = [10, 20, 30, 40, 50, 60]
print(solution(strings, numbers))

# --- Test Cases --- #
strings = 'abcdef'
numbers = [10, 20, 30, 40, 50, 60]
assert solution(strings, numbers) == ('', [10, 20, 30, 40, 50, 60]), "Failed Test 1"

strings = 'xyzabc'
numbers = [10, 20, 30, 40, 50, 60]
assert solution(strings, numbers) == ('wxy', [40, 50, 60]), "Failed Test 2"

strings = 'bcdefg'
numbers = [30, 40, 35]
assert solution(strings, numbers) == ('ab', [35]), "Failed Test 3"
