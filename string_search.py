# --- Nested Loop Challenges ---- #
# build a function that takes two arrays as inputs
# arrays: source_array, search_array
# each array is a tuple containing an integer(ID) and a string

# If ID of  source_array < ID of  search_array
# return array from sourceArray that contains substring of SearchArray

# retain original order
# No match returns an empty array
# items should only be added once

def string_search(source_array, search_array):
    new_array = []

    for index, item in source_array:
        for id, search_val in search_array:
            if index < id and item in search_val:
                if (index, item) not in new_array:
                    new_array.append((index, item))

    return new_array



source_array = [(2, "cat"), (3, "dog")]
search_array = [(3, "catalog"), (4, "gooddog")]

print(string_search(source_array, search_array))

# ---- Test Cases --- #
sourceArray = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
searchArray = [(4, 'abcd'), (5, 'bcda')]
expected_output = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
assert string_search(sourceArray, searchArray) == expected_output, "Failed Test 1"

sourceArray = [(1, 'var'), (2, 'ans'), (3, 'tes')]
searchArray = [(4, 'variant'), (5, 'answertest'), (6, 'tesla')]
expected_output = [(1, 'var'), (2, 'ans'), (3, 'tes')]
assert string_search(sourceArray, searchArray) == expected_output, "Failed Test 2"

sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
searchArray = [(4, 'abcdefghi'), (5, 'defghiabc')]
expected_output = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
assert string_search(sourceArray, searchArray) == expected_output, "Failed Test 3"

sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi'), (4, 'jkl')]
searchArray = [(5, 'mnopqr')]
expected_output = []
assert string_search(sourceArray, searchArray) == expected_output, "Failed Test 4"