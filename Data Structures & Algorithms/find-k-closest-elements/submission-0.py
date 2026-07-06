class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        will be using a minheap for this one
        we want to return the ints in arr that are k closest
        we can package each value in the array into a tuple that is (distance, value)
        put it all into a min heap
        pop the min heap k times
        return them
        """
        minheap = []
        output = []
        for num in arr:
            distance = abs(num - x)
            heapq.heappush(minheap, (distance, num))
        
        for _ in range(k):
            output.append(heapq.heappop(minheap)[1])
        
        return sorted(output)