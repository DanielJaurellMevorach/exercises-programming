# Write your code here

"""def word_count(string):
    return len((string.replace(".", " ")).split(" ")) if len(string) > 0 else 0
"""

def word_count(string):
    return len((string.replace(".", " ")).split(" ")) if len(string) > 0 else 0

print(word_count(""))
