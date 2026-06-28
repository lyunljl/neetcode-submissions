class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMax = 1
        currMin = 1
        for num in nums:
            temp = currMax * num
            currMax = max(num, num * currMax, num * currMin)
            currMin = min(temp, num, num * currMin)
            result = max(result, currMax)
        return result