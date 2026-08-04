class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # left size
        self.minHeap = [] # right side
        

    def addNum(self, num: int) -> None:

        if not self.minHeap or num <= -1*self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -1*num)
        else: # where minHeap has stuff ND the num is > the top value in maxHeap
            heapq.heappush(self.minHeap, num)

        # rebalncing check
        if len(self.maxHeap) - 1 > len(self.minHeap): # if the left side is greater than the right side by more than 1
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - 1 > len(self.maxHeap): # if the right side is greater than the left side by more than 1
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0: # if total value count is even
            return (-1*self.maxHeap[0] + self.minHeap[0]) / 2 #return mean of the top of the two heaps
        else:
            if len(self.maxHeap) > len(self.minHeap):
                # return heapq.heappop(self.maxHeap) * -1
                return -1 * self.maxHeap[0]
            else:
                # return heapq.heappop(self.minHeap)
                return self.minHeap[0]
        