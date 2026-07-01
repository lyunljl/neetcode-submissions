class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        height = height of the second largest out of the 2 we chose
        width  = index1 - index2
        water  = height x width

        We want to maximize the amount of water.
        how do we detemrine how to move the pointers?
        """
        left = 0
        maxA = 0
        right = len(heights) - 1

        while left < right:

            area = (right - left)*min(heights[left], heights[right])
            maxA = max(maxA, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxA