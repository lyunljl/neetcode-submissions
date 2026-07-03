class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                output = min(output, nums[left])
                break

            m = (left + right) // 2
            output = min(output, nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1

        return output                   
        