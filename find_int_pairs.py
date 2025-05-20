# --- Nested Loop Challenges ---- #
# Challenge:
# write a findunction that identifies pairs of integers where a > b
# Pairs can not occur more than once
# Pairs should be tuples
# the order retains in which it appears in listA 

def find_pairs(listA, listB):
    pair_list = []

    for a  in listA:
        for b in listB:
            if a > b and (a, b) not in pair_list:
                pair_list.append((a, b))

    return pair_list


listA = [5, 1, 8, -2, 0]
listB = [3, 2, 7,  10, -1]
expected = [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)]
print(find_pairs(listA, listB))

# --- Test Cases --- #

assert find_pairs([3, 2, 1], [1, 2, 3]) == [(3, 1), (3, 2), (2, 1)], "Failed Test 1"
assert find_pairs([0], [0]) == [], "Failed Test 2"
assert find_pairs([500, 200, -400, -700], [200, -300, 400, -500, 700]) \
    == [(500, 200), (500, -300), (500, 400), (500, -500), (200, -300), \
        (200, -500), (-400, -500)], "Failed Test 3"
assert find_pairs([1000] * 50, [-1000] * 50) == [(1000, -1000)], "Failed Test 4"