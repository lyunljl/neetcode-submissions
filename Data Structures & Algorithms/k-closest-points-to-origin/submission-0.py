class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        my initial thought is to calculate the distance between every point
        from zero, store the actual distance tied with the point somehow,
        return top 3...

        better option is to calculate the distance from 0 to point of each point
        store them in a minheap and then top k distances will be the answer..

        however I need a way to track distances associated to point...
        we can use a hashmap/dict where we map distance --> point
        we take the distances and return associated value in hashmap..
        -- concern if there are multiple points at the same distance....
            -- nvm heaps can already handle dupes just append tuples...
        """

        output = []
        def calculate_distance_origin(point1):
            distance = point1[0]**2 + point1[1]**2
            return distance
        
        min_heap = []
        for point in points:
            temp = (calculate_distance_origin(point), point)
            min_heap.append(temp)
        
        heapq.heapify(min_heap)

        for i in range(k):
            output.append(min_heap[0][1])
            heapq.heappop(min_heap)


        return output
        


