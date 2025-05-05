class TwoSum:
     def __init__(self, numbers, target):
         self.numbers = numbers
         self.target = target
 
     def find_pair(self):
         seen = {}
 
         for index, num in enumerate(self.numbers):
             complement = self.target - num
             
             if complement in seen:
                 return seen[complement] + 1, index + 1
             
             seen[num] = index
         
         return None
 
 numbers = [90, 20, 10, 40, 50, 60, 70]
 target = 50
 solver = TwoSum(numbers, target)
 result = solver.find_pair()
 print(result)