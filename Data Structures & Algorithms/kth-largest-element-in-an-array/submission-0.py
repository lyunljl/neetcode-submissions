class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        brute force solution for funzies
        take array ... sort it
        return the kth largest element
        """
        return sorted(nums)[-k]