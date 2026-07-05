class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = ""
        heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(heap, (count, char))

        #now we have an output and a fully set up max-heap

        while heap:
            count, char = heapq.heappop(heap)
            if len(output) > 1 and output[-1] == output[-2] == char:
                #the senerio where we have soemthing like cc and the top val is c
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                output += char2
                count2 += 1
                if count2 != 0:
                    heapq.heappush(heap, (count2, char2))
                heapq.heappush(heap, (count, char))
            else: #if all is good and dandy
                output += char
                count += 1
                if count != 0:
                    heapq.heappush(heap, (count, char))

        return output
