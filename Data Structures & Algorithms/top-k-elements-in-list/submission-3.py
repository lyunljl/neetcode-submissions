class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # eduardo
        # make a hashmap (key,value) -> (integer, count)
        # keep track of each key's count in nums
        # if len(output) != k and max(key) not in output add the max to output
        num_count = {}
        output = []
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        
        for i in range(k):
            highest_count = max(num_count, key=num_count.get)
            output.append(highest_count)
            num_count.pop(highest_count, None)
        
        return output
        
