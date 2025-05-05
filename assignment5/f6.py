def add_ing(s):
    if len(s) >= 3:
        return s + 'ly' if s.endswith('ing') else s + 'ing'
    return s
print(add_ing('abc'))
print(add_ing('string'))
