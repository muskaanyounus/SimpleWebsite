def smallest_largest_words(s):
    words = s.split()
    smallest = min(words, key=len)
    largest = max(words, key=len)
    return smallest, largest
print(smallest_largest_words("This is a sample sentence for testing"))
