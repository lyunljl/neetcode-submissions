class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [2, 4, -3, 5, 10]
        #brute force it
        res = nums[0]

        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res

        