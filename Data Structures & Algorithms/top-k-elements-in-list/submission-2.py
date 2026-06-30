class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        gonna solve this using heaps
        we want to use max-heaps but we only have minheaps. 

        we will make a dict to track numbers-->freq
        then turn it into tuples of (freq, number)
        all into a list.. heapify it
        pop k times
        """
        freq = {} # numer --> freq
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        heap = [] #aka a prioirty queue
        for num, freq in freq.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output