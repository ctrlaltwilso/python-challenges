# ---- Nested Loops ---- #
# Challenge:
# provided two arrays of unique integers
# identify elements that appear in both arrays
# return elements in an array

def common_elements(listA, listB):
    common = []

    for a in listA:
        for b in listB:
            if a == b:
                common.append(a)

    return common

listA = [7, 2, 3, 9, 1]
listB = [2, 3, 7, 6]

print(common_elements(listA, listB))

assert common_elements([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]) == [], "Test Failed"
assert common_elements([1, 2, 3], [2, 3, 4, 1]) == [1, 2, 3], "Test Failed"
assert common_elements([1, 2, 3], [3, 2, 1, 4, 5, 6]) == [1, 2, 3], "Test Failed"