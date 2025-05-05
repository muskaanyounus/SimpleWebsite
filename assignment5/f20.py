def remove_consec_duplicates(s):
    result = s[0]
    for c in s[1:]:
        if c != result[-1]:
            result += c
    return result
print(remove_consec_duplicates("aaabbbcccaaa"))
