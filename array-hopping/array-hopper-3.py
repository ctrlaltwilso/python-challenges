# ---- Array Hopping Challenges ---- #
# Challenge:
# Funcation that has two list inputs (roadA, roadB)
# Calculate and return total distance during hop sequence
# each hop == 1 distance
# Return once a hop is repeated
# Keep track of index hops seperately from A and B
# each value is a valid index in the other list

def solution(roadA, roadB):
    final_output = []

    for i in range(0, len(roadA)):
        visited = set()
        distance = 0
        position = i
        is_on_roadA = True

        while True:
            if (position, is_on_roadA) in visited:
                final_output.append(distance)
                break
            else:
                if is_on_roadA:
                    visited.add((position, is_on_roadA))
                    position = roadA[position]
                    distance += 1
                    is_on_roadA = False
                else:
                    visited.add((position, is_on_roadA))
                    position = roadB[position]
                    distance += 1
                    is_on_roadA = True

    return final_output

roadA = [1, 0, 2]
roadB = [2, 0, 1]
print(solution(roadA, roadB))

# ---  Test Cases --- #
roadA = [0, 0, 0, 0, 0]
roadB = [0, 0, 1, 2, 3]
expected = [2, 3, 3, 3, 3]
assert solution(roadA, roadB) == expected, "Failed Test 1"

roadA = [2, 2, 2, 2]
roadB = [3, 2, 1, 0]
expected = [3, 2, 3, 3]
assert solution(roadA, roadB) == expected, "Failed Test 2"

roadA = [1, 2, 3, 0]  
roadB = [2, 3, 0, 1] 
expected = [8, 8, 8, 8]
assert solution(roadA, roadB) == expected, "Failed Test 3"

roadA =[1, 2, 1] 
roadB = [0, 2, 1]
expected = [3, 2, 2] 
assert solution(roadA, roadB) == expected, "Failed Test 4"