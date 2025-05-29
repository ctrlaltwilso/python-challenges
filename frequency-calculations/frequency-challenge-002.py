# ---- Frequency Challenge ---- #
# Challenge:
# Return  dictionary
# Each key-value pair represents letter(k) and numerical value (v)
# v calculated by shifting letter by 3 positions backward(wrapped around)
# Then multiple the ASCII value of new char by frequency of k
# chars only lowercase

def solution(s):
    final_output = {}

    for char in set(s):
        count = s.count(char)
        shifted = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        calc = count * ord(shifted)
        final_output[char] = calc
        
    return final_output

print(solution('abc'))

# --- Test Cases --- # 
assert solution("def") == {'d': 97, 'e': 98, 'f': 99}, "Failed Test 1"
assert solution("aabccc") == {'a': 240, 'b': 121, 'c': 366}, "Failed Test 2"
assert solution("zzzzzzzzzz") == {'z': 1190}, "Failed Test 3"
assert solution("xyzaaxz") == {'a': 240, 'x': 234, 'y': 118, 'z': 238}, "Failed Test 4"