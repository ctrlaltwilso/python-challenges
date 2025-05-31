# ---- Conditional Interruption Challenges ---- #
# Challenge: 
# Create function that acceptsa string and array of numbers
# String: 
#   Replace ever occurrence of a vowel with next vowel in sequence
#   Consonants: replace each with the next in series

# Numbers: Multiple each integer by  3 and add to total. 
    # Stop when total reaches or exceeds 100
# Return:  MOdified string and any unprocessed integers

def  solution(inputString, numbers):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    total = 0
    result = ''
    i = 0

    while i <  len(inputString) and i < len(numbers) and total <= 100:
        total += numbers[i] * 3
        if inputString[i].isalpha():
            if inputString[i] in vowels:
                index = (vowels.index(inputString[i]) + 1) % len(vowels)
                result += vowels[index]
            else:
                index = (consonants.index(inputString[i]) + 1) % len(consonants)
                result += consonants[index]
        i += 1
    
    return result, numbers[i:]

input_string = 'negative'
array = [-1, -2, -3, -4, -5, -6, -7, -8]
print(solution(input_string, array))

# --- Test Cases --- #
input_string = 'zero'
array = [0, 0, 0]
expected_output = ('bis', [])
assert solution(input_string, array) ==  expected_output, "Failed Test 1"

input_string = 'abc'
array = [10, 20, 30, 40, 50]
expected_output = ('ecd', [40, 50])
assert solution(input_string, array) ==  expected_output, "Failed Test 2"

input_string = 'abcdefghijk'
array = [5, 10]
expected_output = ('ec', [])
assert solution(input_string, array) ==  expected_output, "Failed Test 3"

input_string = 'a'
array = [100]
expected_output = ('e', [])
assert solution(input_string, array) ==  expected_output, "Failed Test 4"