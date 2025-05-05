def is_balanced(s):
     stack = []
     delimiter_map = {')': '(', '}': '{', ']': '['}
     
     for char in s:
         if char in "({[":
             stack.append(char)
         elif char in ")}]":
             if not stack or stack[-1] != delimiter_map[char]:
                 return False 
             stack.pop()  
     
 
     return len(stack) == 0
 
 print(is_balanced("([{}])"))  
 print(is_balanced("([)]"))   
 print(is_balanced("([]"))     
 print(is_balanced("[]"))      
 print(is_balanced("([})"))
