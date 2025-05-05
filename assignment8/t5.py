class ThreeSum:
     def __init__(self, nums):
         self.nums = sorted(nums)
 
     def find_triplets(self):
         result = []
         n = len(self.nums)
 
         for i in range(n - 2): 
             if i > 0 and self.nums[i] == self.nums[i - 1]:
                 continue
 
             left, right = i + 1, n - 1
 
             while left < right:
                 total = self.nums[i] + self.nums[left] + self.nums[right]
                 if total == 0:
                     result.append([self.nums[i], self.nums[left], self.nums[right]])
                     while left < right and self.nums[left] == self.nums[left + 1]:
                         left += 1
                     while left < right and self.nums[right] == self.nums[right - 1]:
                         right -= 1
                     left += 1
                     right -= 1
                 elif total < 0:
                     left += 1
                 else:
                     right -= 1
         return result
 
 numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
 solver = ThreeSum(numbers)
 result = solver.find_triplets()
 print(result)