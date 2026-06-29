class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        challenge: find without using sort
        use a heap, it will maintain a minheap.
        iterate through nums and add to minheap 
        if len of minheap passes k we pop 

        return minheap of 0 becuase there are k elements in heap the "smallest" === "kth largest"
        """

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
