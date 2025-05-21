# find all instances of each word in corresponding sentences
# each word is associated with only one sentence
# all words in 'words' will be lowercase
# reverse the search word
# if word not found keep as is
# perserve the case of initial letter of word(if captialize)

# example:  
# sentences = ["look at that cat", "Dogs are great"]
# words = ["cat", "dog"]
# Output = ["Look a that Tac", "Sgod are great"]

def reverse_word(sentences, words):
    new_vals = []
    
    for sentence, word in zip(sentences, words):
        rev_word = word[::-1]
        sentence = sentence.replace(word, rev_word)
        sentence = sentence.replace(word.capitalize(), rev_word.capitalize())
        new_vals.append(sentence)
    
    return new_vals

print(reverse_word(["Look at that cat", "Dogs are great"],  ["cat", "dogs"]))