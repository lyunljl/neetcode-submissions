class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        elif len(set(nums)) > len(nums):
            return "Bad Input"
        else:
            return False
         