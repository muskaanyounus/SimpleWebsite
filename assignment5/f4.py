def change_char(s):
    return s[0] + s[1:].replace(s[0], '$')
print(change_char('restart'))
