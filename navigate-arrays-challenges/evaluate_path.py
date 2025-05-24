# ---- Navigate Arrays Challeng ---- #
# Challenge:
# Traverse the array indexes by the val of the integer
# Positive values move index to the right
# negative indexes move to the left
# only allowed two direction changes
# if the value is 0, the traversal ends

def evaluate_path(numbers):
    position = 0
    moves = 0
    direction = 1
    direction_change = 0

    while True:
        if numbers[position] == 0:
            return (position, moves)
        
        step = numbers[position] * direction
        new_position = position + step
        if new_position < 0 or new_position >= len(numbers):
            direction *= -1
            direction_change += 1
            if direction_change >= 2:
                return (position, moves)
        else:
            position = new_position
            moves += 1

print(evaluate_path([2, 1, -3, 4]))

# --- Test Cases --- #
assert evaluate_path([0]) == (0, 0), "Failed Test 1"
assert evaluate_path([3, 4, 1, 1, -3, 1]) == (4, 5), "Failed Test 2"
assert evaluate_path([3, -3]) == (0, 0), "Failed Test 3"
assert evaluate_path([3, 2, -1, 2, 2, -1, 4]) == (1, 7), "Failed Test 4"

