class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    #eduardo
    #need a priority queue 
    #keep track of the current max (via max-heap)
    #compare the stones at of top priority
    #iterate until all stones are gone
    #heapify for min heap (heapq.heapify) use negatives for max heap
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            #gets two heaviest stones
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            if stone1 != stone2:
                heapq.heappush(max_heap, -abs(stone2-stone1))

        if max_heap:
            return -max_heap[0]
        else:
            return 0
            