class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        optimized solution
        we can optimize the previous solution by taking advantage of it
        already being sorted.

        since its sorted we know that going up means increasing
        likewise going down means its decreasing

        start the two pointers on oppisite ends
        at each round check if the current sum is greater than or less than target
        if its less than we know that we have to move the left pointer up to "up the sum"
        else: we know to decrease the right poitner to "lower the sum"
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return