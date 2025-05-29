# ---- Frequency Challenge ---- #
# Challenge: 
# function accepts a sentence
# chars contain a-z, A-Z, 0 - 9
# shift each character back by 1
# Count the frequency of each character
# Subtract frequency from each char, convert all chars to ascii
# return array listed in ascending order

def solution(s):
    final_output = []
    shifted_s = []

    for char in s:
        if char.isalpha():
            if char.isupper():
                shifted_letter = chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
                shifted_s.append(shifted_letter)
            else:
                shifted_letter = chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
                shifted_s.append(shifted_letter)

        elif char.isdigit():
            shifted_num = chr((ord(char) - ord('0') - 1) % 10 + ord('0'))
            shifted_s.append(shifted_num)

    for char in set(shifted_s):
        count = shifted_s.count(char)
        final_output.append(ord(char) - count)
    
    final_output.sort()
    return final_output

print(solution("Hello, 123!"))

# --- Test Cases --- #
assert solution("Once upon a time, in a galaxy far, far away...") == [77, 97, 98, 99, 101, 102, 106, 106, 107, 109, 110, 111, 114, 114, 115, 117, 118, 118], "Failed Test 1"
assert solution("When in the course of human events...") == [85, 95, 97, 100, 100, 103, 105, 107, 108, 112, 112, 113, 114, 116, 121], "Failed Test 2"
assert solution("The quick brown fox jumps over the lazy dog.") == [82, 96, 97, 97, 98, 100, 101, 101, 103, 104, 105, 106, 106, 107, 108, 110, 111, 111, 113, 114, 114, 116, 117, 118, 119, 120, 121], "Failed Test 3"
assert solution("fedcba") == [96, 97, 98, 99, 100, 121], "Failed Test 4"