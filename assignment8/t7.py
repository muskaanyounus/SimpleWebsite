class StringReverser:
     def reverse_words(self, s: str) -> str:
         words = s.strip().split()
         reversed_words = words[::-1]
         return ' '.join(reversed_words)
 
 
 reverser = StringReverser()
 input_string = 'hello .py'
 output = reverser.reverse_words(input_string)
 print(output) 