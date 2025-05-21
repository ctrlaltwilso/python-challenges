# Accepts input as text, old and new
# replaces every occurrence of  old in text with new
# returns updated text string with all replaced substrings

def replace_substring(text, old, new):
    return text.replace(old, new)

print(replace_substring("hello world", "world", "friend"))
