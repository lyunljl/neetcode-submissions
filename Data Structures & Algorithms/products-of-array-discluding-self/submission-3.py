class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        ussually i would just multiply all values in list together then divide by i....

        intitialze output array = []
        inititalize pre/postfix = 1
        forward pass and get product of all values up to "i"
            replace spot in output with it's prefix so all vals up to that spot
            calculate product of all vals in nums up to index
        repeat for postfix
    
        '''
        output = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix # populates current spot with previous product value
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output