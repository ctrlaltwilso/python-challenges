# ---- Large Numbers as Strings Challenges ---- #
# Challenge: 
# Function that compares two "string-numbers" without converting to int. 
# can only use comparison operators (<, >, ==) on strings.
# compare to most significatn to least significant digit
# If num1 > num2:
    # return 1
# if num1 < num2:
    # return -1
# if num1 == num2:
    # return 0

def solution(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1

    if i == j:
        for n in range(i + 1):
            if num1[n] > num2[n]:
                return 1
            elif num1[n] < num2[n]:
                return -1
        else:
            return 0
    elif i > j:
        return 1
    else:
        return -1


print(solution("1234", "1235"))


# --- Test Cases --- #
assert solution('1234', '12345') == -1, "Failed Test 1"
assert solution('12345', '12345') ==  0, "Failed Test 2"
assert solution('100', '101') == -1, "Failed Test 3"
assert solution('600', '600') == 0, "Failed Test 4"