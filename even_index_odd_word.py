# ---- Nested Loop Challenges ---- # 
# Problem: 
# Create function that selects even-indexed chars of words containing odd length
# final output will be reversed end-to-end
# output is a string
# does not need to include spaces

def even_index_odd_word(sentence):
    final_output = []

    words = sentence.split(' ')

    for word in words:
        index = 0
        if len(word) % 2 == 1:
            for char in word:
                if index % 2 == 0:
                    final_output.append(char)
                index += 1

    return ''.join(final_output[::-1])

print(even_index_odd_word("fun time rodeo"))


# --- Test Cases --- #
assert even_index_odd_word("Coding tasks are fun and required") == "danfeasst", "Failed Test 1"
assert even_index_odd_word("python coding") == "", "Failed Test 2"
assert even_index_odd_word("star wars") == "", "Failed Test 3"
assert even_index_odd_word("Hello, world!") == "", "Failed Test 4"