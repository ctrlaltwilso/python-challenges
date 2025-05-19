import unittest
# spot_swaps -> two  strings, source and target
# only lowercase english letters
# return list of tuples: 
#   zero-based index of swap
#   the character at index 
#   charcter that swapped with target

# Rules:
# characters can be swapped only once
# swapped characters returned in a list the order they were found
# don't check f or  swaps at the last position of a string

# example:
# source = "hello"
# target = "hlelo"
# output: [(1, 'e', 'l')]

def spot_swaps(source: str, target: str) -> list:
    output = []

    for i in range(len(source) - 1):
        if source[i] != target[i] and source[i+1] == target[i] \
            and source[i] == target[i+1]: 
            output.append((i, source[i], target[i]))
    
    return output

print(spot_swaps("hello",  "hlelo"))
print(spot_swaps("abcdeg", "abcfed"))

# Tests
assert spot_swaps("hello",  "hlelo") == [(1, 'e', 'l')], "test failed"
assert spot_swaps("abcdef", "abcfed") == [], "test failed"