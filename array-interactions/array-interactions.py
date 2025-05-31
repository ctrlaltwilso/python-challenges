# ---- Array Interactions Challenge 001 --- #
# Challenge
# Form neighbouring  pairs in a string sequentially
# Each pair, compare the characters and remove the lower char
    # If same, remove the first char in pair
# Perform steps  until the string becomes empty
# if the string length after round is 1, the last char is removed and process terminates


def solution(s):
    remaining_char = list(s)
    removed = []
    
    while len(remaining_char) > 0:
        if len(remaining_char) == 1:
            removed.append(remaining_char[0])
            break

        next_round = []
        i = 0

        while i < len(remaining_char) - 1:
            a, b = remaining_char[i], remaining_char[i+1]
            if a <= b:
                removed.append(a)
                next_round.append(b)
            else:
                removed.append(b)
                next_round.append(a)
            i += 2
        if i < len(remaining_char):
            next_round.append(remaining_char[-1])
        remaining_char = next_round
        
    return removed

# --- Test Cases --- #
assert solution('BCAAB') == ['B', 'A', 'A', 'B', 'C'], "Failed Test 1"
assert solution('AB') == ['A', 'B'], "Failed Test 2"
assert solution('ABCDE') == ['A', 'C', 'B', 'D', 'E'], "Failed Test 3"