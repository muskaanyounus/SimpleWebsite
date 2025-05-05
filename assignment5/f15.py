from collections import Counter
s = 'thequickbrownfoxjumpsoverthelazydog'
freq = Counter(s)
for char, count in freq.items():
    if count > 1:
        print(char, count)
