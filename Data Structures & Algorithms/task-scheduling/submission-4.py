class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
        the wat to optimize the time needed is to start... we can keep track of which letter
        is currently most frequent using a max-heap
        ... how do we track when an item can be reused?
        """
        counter = {}
        daheap = []
        for task in tasks:
            if task not in counter:
                counter[task] = 1
            else:
                counter[task] += 1

        for task, freq in counter.items():
            heapq.heappush(daheap, -freq)
    
        daqueue = deque() # this will store tuples that track (value, time of return)
        time = 0

        while daheap or daqueue:
            time += 1
            if daheap:
                count_left = 1 + heapq.heappop(daheap)
                if count_left:
                    daqueue.append([count_left, time + n])
            
            if daqueue and daqueue[0][1] == time:
                heapq.heappush(daheap, daqueue.popleft()[0])
                
        return time