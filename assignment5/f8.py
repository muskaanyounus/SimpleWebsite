def longest_word(words):
    return max(len(word) for word in words)
print(longest_word(['apple', 'banana', 'cherry', 'date']))
