# ---- Nested Loop Challenges ---- #
# Challenge:
# Split even words in string
# Then split words in half that are even length
# if the ord(char) is less than ord(c)
    # add to output
# ASCII char from ' '  to '~'
# differentiate between upper and lower

def split_ascii(sentence, c):
    final_output = []
    c = ord(c)
    words = sentence.split()

    for word in words:
        mid = len(word) // 2
        if len(word) % 2 == 0:
            for char in word[mid:]:
                if ord(char) < c:
                    final_output.append(char)

    return ''.join(final_output)

print(split_ascii("Python", "n"))

# --- Test Cases --- #
assert split_ascii("Practice makes perfect.", 'f') == \
                "ceec.", "Failed Test 1"
assert split_ascii("I will pass this test!", 'w') == \
            "llssis", "Failed Test 2" 
assert split_ascii("Participate in exciting challenges.", 'a') == \
            "", "Failed Test 3"
assert split_ascii("The quick brown fox jumps over the lazy dog.", 'f') == \
            "e.", "Failed Test 4"