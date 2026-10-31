class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #eduardo 
        previous_nums = []
        for num in nums:
            if num in previous_nums:
                return True  
            previous_nums.append(num) 
        return False