def upper_if_2_upper_in_4(s):
    return s.upper() if sum(1 for c in s[:4] if c.isupper()) >= 2 else s
print(upper_if_2_upper_in_4('ABcdhello'))
print(upper_if_2_upper_in_4('Abcd'))
