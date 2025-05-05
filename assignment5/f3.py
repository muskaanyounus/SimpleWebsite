def first_last_two(s):
    return s[:2] + s[-2:] if len(s) >= 2 else ''
print(first_last_two('thisisniceone'))
print(first_last_two('ab'))
print(first_last_two('f'))
