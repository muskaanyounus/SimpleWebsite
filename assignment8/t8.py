class StringManipulator:
     def __init__(self):
         self.user_string = ""
 
     def get_string(self):
         self.user_string = input("Enter a string: ")
 
     def print_string(self):
         print(self.user_string[::-1])
 
 
 manipulator = StringManipulator()
 manipulator.get_string()
 manipulator.print_string()