import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #eduardo
        # assume for duplicates
        # do this by index, make a new list and take the product of that
        # make a prefix array and store it in i slot so the prefix i goes in i

        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

