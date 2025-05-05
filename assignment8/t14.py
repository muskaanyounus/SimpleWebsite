starts_with = lambda s, char: s.startswith(char)
 
 string = "Python programming"
 char = "P"
 
 print(f"Does '{string}' start with '{char}'? ->", starts_with(string, char))