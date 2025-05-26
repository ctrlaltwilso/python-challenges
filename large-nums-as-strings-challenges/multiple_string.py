# ---- Large Numbers as Strings Challenges ---- #
# Challenge: 
# Function accepts to string parameters
# return product as a string
# multiple each string without converting the entire string to int.

def solution(num1, num2):
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            n1 = int(num1[i])
            n2 = int(num2[j])
            
            result[i + j + 1] += n1 * n2

    carry = 0
    
    for n in range(len(result) - 1, -1, -1):
        result[n] += carry
        carry = result[n] // 10
        result[n] = result[n] % 10

    result = ''.join(str(d) for d in result).lstrip('0')

    return result if result else '0'

print(solution("32", "12"))

# --- Test Cases --- #
assert solution("123", "456") == "56088", "Failed Test 1"
assert solution("1000000000", "1000000000") == "1000000000000000000", "Failed Test 2"
assert solution("0", "500") == "0",  "Failed Test 3"
assert solution("50", "5") == "250", "Failed Test 4"