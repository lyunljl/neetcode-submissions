class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        very similar to cpu task scheduler
        going to turn the entire string into a hashmap

        send the items in hashmap into a max-heap(greedy) as a tuple of (freq, char)

        reconstruct a valid string by
        if string is empty just pop heap and add char to string

        if string is not empty:
            popheap and check char comparison
            if prev char is same as popped val
                if heap is empty
                    return output
                else:
                    new var = popheap again
                    assign to outpit
                    repush old popped val back on heap
        """

        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        maxHeap = []
        for char, freq in counter.items():
            heapq.heappush(maxHeap, (-freq, char))
        
        output = ""
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if not output:
                output += char
                freq += 1 # +1 since its a maxheap
                if freq != 0:
                    heapq.heappush(maxHeap, (freq, char))
            elif output[-1] == char:
                if maxHeap: #check if another option actually exists
                    freq2, char2 = heapq.heappop(maxHeap)
                    output += char2
                    freq2 +=1 # +1 since its a maxHeap
                    if freq2 != 0:
                        heapq.heappush(maxHeap, (freq2, char2))
                    heapq.heappush(maxHeap, (freq, char))
                else:
                    return ""
            else: #if all is good and dandy
                output += char
                freq += 1 # +1 since its a maxHeap
                if freq != 0:
                    heapq.heappush(maxHeap, (freq,char))
        return output
                
        
