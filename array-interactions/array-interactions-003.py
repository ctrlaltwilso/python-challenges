# ---- Array Interactions Challenge 003 ---- #
# Challenge:
# function accepts an array
# transfer the first digit to the right most digit
    # first position
# the amount of transfer times is equal to the length of longest digit

def house_game(houses):
    string_houses = [str(h) for h in houses]

    max_len = max(len(h) for h in string_houses)
    n = len(houses)

    for i in range(max_len):
        # Step 1: Collect digits to transfer and remove from donor
        transfers = [None] * n
        new_houses = string_houses[:]

        for j in range(n):
            if len(string_houses[j]) >= i + 1:
                transfers[j] = string_houses[j][-(i+1)] # type: ignore
                # Remove the digit from donor
                new_houses[j] = string_houses[j][:-(i+1)] + string_houses[j][-(i):] if i != 0 else string_houses[j][:-1]

        # Step 2: Add the digit to the right neighbor
        for j in range(n):
            if transfers[j] is not None:
                idx = (j + 1) % n
                new_houses[idx] = transfers[j] + new_houses[idx] # type: ignore

        if new_houses == string_houses:
            break
        string_houses = new_houses

    return [int(h) for h in string_houses]

# --- Test Cases --- #
assert house_game([123, 234, 345, 456]) == [362, 433, 144, 255], "Failed Test 1"
assert house_game([12, 34, 56]) == [41, 63, 25], "Failed Test  2"
assert house_game([1, 1, 2, 2, 3, 3]) == [3, 1, 1, 2, 2, 3], "Failed Test 3"