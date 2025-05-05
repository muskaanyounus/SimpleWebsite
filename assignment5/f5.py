def swap_chars(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]
print(swap_chars('abc', 'xyz'))
