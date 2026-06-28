class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        initial reaction is to basically sort, pop last 2 elements
        smash, re-add any remainders, resort,
        repeat until we have either 1 or nothing left. 
        this is n times nlogn time.

        we can use a max-heap to be more efficent, 
        the top elements will always be the max 
        so while len(heap) > 1
        popheap once popheap twice
        calculate difference
        heap push differeance

        this repeats until heap len is <= 1 which then it stops
        return wieght of last stone or just 0 if len(heap) == 0
        """

        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) 
            stone2 = heapq.heappop(max_heap)

            if stone1 != stone2:
                heapq.heappush(max_heap, -abs(stone1 - stone2))

        if max_heap:
            return -max_heap[0]
        else:
            return 0
