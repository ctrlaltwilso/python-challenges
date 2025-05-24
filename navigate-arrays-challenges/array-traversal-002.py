# ---- Navigate Arrays Challenges ---- #
# Challenge: 
# Returns array 'moves'
# for every i in  move, the algorithm should calculate the number of moves to exit 'board'/list
# If  encounter an obstacle, moves[i] = -1
# obstacles are defined as an input parameter 

def solution(board, obstacle):
    moves = []
    
    for i in range(len(board)):
        position = i
        val = 0
        
        while True:
            if position >= len(board):
                moves.append(val)
                break
            elif board[position] == obstacle:
                moves.append(-1)
                break
            else:
                position += board[position]
                val += 1
                
    return moves

print(solution([5, 3, 2, 6, 2, 1, 7], 3))

# --- Test Cases ---  # 
assert solution([5, 3, 2, 6, 2, 1, 7], 3) == [3, -1, 3, 1, 2, 2, 1],  "Failed Test 1"
assert solution([1, 1, 1, 1, 1], 1) == [-1, -1, -1, -1, -1], "Failed Test 2"
assert solution([i for i in range(1, 11)]*2, 1) == [-1, 4, 5, 3, 3, 4, 3, 2, 2, 2, -1, 3, 2, 2, 2, 1, 1, 1, 1, 1], "Failed Test 3"
assert solution([1]*500, 1) == [-1]*500, "Failed Test 4"