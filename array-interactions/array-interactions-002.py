# --- Array Interactions Challenge 002 --- #
# Challenge:
# Game consist of  rounds
# Each knight fights knight on left(loopback for end)
# subtract value(strength) from grouped knights
# if knight strength becomes equal or less than 0
    # remove knight
# Game continues until no more matches can be made
# return number of rounds

def tournament(knights):
    rounds = 0
    
    while knights:
        next_round = []
        i = 0

        if len(knights) == 1:
            return rounds
            break

        while i < len(knights):
            strength = knights[i] - knights[(i + 1) % len(knights)]
            if strength > 0:
                next_round.append(strength)
            i += 1
        knights = next_round
        rounds += 1

# --- Test Cases --- #
assert tournament([100, 50, 30, 20]) == 3, "Failed Test 1"
assert tournament([70, 80, 60]) == 1, "Failed Test 2"
assert tournament([90, 10, 30]) == 1, "Failed Test 3"