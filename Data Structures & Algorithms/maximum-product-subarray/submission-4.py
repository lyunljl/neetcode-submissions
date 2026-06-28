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

"""
a dynamic programming approach tracks both the current maximum product (currMax) 
and the current minimum product (currMin) at each step. 
This dual tracking is essential because a highly negative minimum can instantly flip 
into a massive positive maximum when multiplied by another negative number. 
By continually updating these two boundaries alongside a global result using the current 
number alone, the running maximum streak, or the negative-flip potential, 
the algorithm efficiently solves the problem in $O(n)$ time and $O(1)$ space.
"""