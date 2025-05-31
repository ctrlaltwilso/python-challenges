# ---- Navigating with Variables Challenge 002 ---- #
# Challenge
# Given a jardin with flowers
# each  flower represents a 1D array
    # index = location
    # value = flower type
# the function accepts a start and a direction
    # right = 1, left = -1
# return the largest step so that every flower type is visited

def largest_step(garden, start, direction):
    flower_types = set(garden)

    for step in range(len(garden), 0, -1):
        position = start
        visited = set()
        while 0 <= position < len(garden):
            visited.add(garden[position])
            position += step * direction

        if visited == flower_types:
            return step
                        
    return -1

# --- Test Cases --- #
assert largest_step([3, 1, 2, 1, 3, 2, 1], 0, 1) == 2,  "Failed Test 1"
assert largest_step([1, 2, 3, 4, 5, 9, 2, 1, 3, 8, 2, 7, 1, 6], 13, -1) == 1, "Failed Test 2"
assert largest_step([1, 2, 3, 4, 5], 0, 1) == 1, "Failed Test 3"
assert largest_step([1, 5, 2, 5, 3, 5, 4, 5], 3, -1) == -1, "Failed Test 4"