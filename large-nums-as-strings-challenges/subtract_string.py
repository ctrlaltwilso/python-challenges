# ---- Large Number as Strings Challeneges ---- #
# Challenge:
# Subtract num2 from num1 with  out directly converting the strings to integers
# Subtraction will not result in a negative number

def solution(num1, num2):
    i, j, carry, res = len(num1) - 1, len(num2) -1, 0, []

    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        total = (n1 - n2) - carry
        if n1 < n2 + carry:
            carry = 1
            total += 10
        else:
            carry = 0
        
        curr = total % 10
        res.append(str(curr))
        i, j = i -1, j -1

    result = ''.join(res[::-1]).lstrip('0')
    return result if result else '0'


print(solution('398746', '199234'))

# --- Test Cases --- #
assert solution('100', '1') == '99', "Failed Test 1"
assert solution('9', '1') == '8', "Failed Test 2"
assert solution('1000', '800') == '200', "Failed Test 3"
assert solution('150', '100') == '50', "Failed Test 4"