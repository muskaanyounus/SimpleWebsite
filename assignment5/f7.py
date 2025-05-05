def not_poor_replace(s):
    n = s.find('not')
    p = s.find('poor')
    if n != -1 and p != -1 and p > n:
        return s[:n] + 'good' + s[p+4:]
    return s
print(not_poor_replace('The lyrics is not that poor!'))
print(not_poor_replace('The lyrics is poor!'))
