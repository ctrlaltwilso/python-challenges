# ---- Navigating with Variables Challenges ---- #
# Challenge: 
# Traverse an input array of integers
    # integers represent traps in a dungeon
    # Each trap reduces health(input parameter)
# If health < 0 increase step
# Find the amount of step intervals to traverse with the most remaining health
# Step must be < len(dungeon)

def solution(dungeon, health):
    step = 1
    best_step = (0, 0)

    while step <= len(dungeon):
        current_health = health
        for i in range(0, len(dungeon), step):
            current_health -= dungeon[i]
            if current_health < 0:
                break
        if best_step[1] < current_health:
            best_step = (step, current_health)
        step += 1
    
    return best_step[0]

dungeon = [0, 5, -2, 8, 3, 0, 10, 4, -1, 7]
health = 20

print(solution(dungeon, health))

# --- Test Cases --- #
assert solution([0, -1, 1, 0, -1], 3) == 1, "Failed Test 1"
assert solution([1, 0, -1, 1, 0], 5) == 2, "Failed Test 2"
assert solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == 10, "Failed Test 3"
assert solution([1, 2, 3, 4, 5], 20) == 5, "Failed Test 4"