class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        we can use a heap and sort by freq, digit
        """
        freq = {}
        for number in nums:
            if number not in freq:
                freq[number] = 1
            else:
                freq[number] += 1
        
        output = []
        for number, freq in freq.items():
            if freq > len(nums) // 3:
                output.append(number)
        return output
