class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # self.nums = nums
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k: #if the size of heap is bigger than k we can keep popping until up to k size
            heapq.heappop(self.minHeap) # this is really useful because we know that we will only pop the smallest element.
            

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #push val on to the minHeap
        if len(self.minHeap) > self.k: #if minHeap is is longer than k we pop the minval (not needed anyways)
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #minimum from heap will always be on top

[1,2,3,3,0]
