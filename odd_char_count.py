# ---- Nested Loop Challenges ---- #
# Challenge: 
# creat a function:
# input: string of words
# Seperate each word
# return the most frequently occurring char in each word that has odd num of chars
# input string contains Upper and Lower, both count as same letter
# In the event of a tie, return the char that appears first
# if no odd words, return empty string
# input string will always be atleast one char long

def odd_char_count(sentence):
    final_output = []
    words = sentence.split()

    for word in words:
        counts = {}
        if len(word) % 2 > 0:
            for char in word:
                c = char.lower()
                if c in counts:
                    counts[c] += 1
                else:
                    counts[c] = 1
                    
            max_val = max(counts.values())
            
            for char in word:
                c = char.lower()
                if counts[c] == max_val:
                    final_output.append(c)
                    break
            
    return ''.join(final_output)

print(odd_char_count("Apple pie is Awesome"))


# --- Test Cases --- #
assert odd_char_count("Python is a high-level programming language") == "ar", "Failed Test 1"
assert odd_char_count("Mastering Advanced Looping and Implementation") == "moa", "Failed Test 2"
assert odd_char_count("nested loops") == "o", "Failed Test 3"
assert odd_char_count("Python") == "", "Failed Test 4"