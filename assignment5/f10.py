words = input("Enter comma-separated words: ")
unique_words = sorted(set(words.split(',')))
print(', '.join(unique_words))
