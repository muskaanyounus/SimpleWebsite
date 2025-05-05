class SubsetGenerator:
     def __init__(self, nums):
         self.nums = nums
 
     def get_subsets(self):
         result = []
         self._backtrack(0, [], result)
         return result
 
     def _backtrack(self, index, current_subset, result):
         result.append(current_subset[:])
 
         for i in range(index, len(self.nums)):
             current_subset.append(self.nums[i]) 
             self._backtrack(i + 1, current_subset, result)  
             current_subset.pop()  
 
 generator = SubsetGenerator([4, 5, 6])
 subsets = generator.get_subsets()
 print(subsets)