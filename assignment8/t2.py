lass ParenthesesValidator:
     def __init__(self):
         self.bracket_pairs = {
             ')': '(',
             '}': '{',
             ']': '['
         }
 
     def is_valid(self, s: str) -> bool:
         stack = []
 
         for char in s:
             if char in '({[':
                 stack.append(char)
             elif char in ')}]':
                 if not stack or stack[-1] != self.bracket_pairs[char]:
                     return False
                 stack.pop()
 
         return not stack
 
 
 validator = ParenthesesValidator()
 
 # Valid cases
 print(validator.is_valid("()"))  
 print(validator.is_valid("()[]{}"))  
 
 # Invalid cases
 print(validator.is_valid("[)"))  
 print(validator.is_valid("({[)]"))  
 print(validator.is_valid("{{{")) 