class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            using bucketsort
        '''
        count = {} # this will map numbers --> its count
        # bucketsort begins here
        freq = []
        for i in range(len(nums) + 1):
            freq.append([]) # list of lists of size len(nums) [[],[],[],[],....[]]
        for n in nums:
            # Count the frequency of each number, safely defaulting to 0 if it's the first occurrence
            count[n] = 1 + count.get(n, 0) 
        for n, c in count.items():
            freq[c].append(n) #appends number to said count
    
        result = []
        for i in range(len(freq)-1, 0 , -1): # start at last index, go to 0 index, count backwards by 1
            for n in freq[i]: # for each list inside the list
                result.append(n) # start adding the list of numbers to output result
                if len(result) == k: # once k numbers have been added. we are done
                    return result

# O(klogn)