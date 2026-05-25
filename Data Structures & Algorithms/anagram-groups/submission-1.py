class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
            
        output = []
        visited = [False] * len(strs) # Track what we've already grouped
        
        for i in range(len(strs)):
            if visited[i]:
                continue
                
            templist = [strs[i]]
            visited[i] = True
            
            for j in range(i + 1, len(strs)): # Start from i + 1 to avoid double checking
                if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                    templist.append(strs[j])
                    visited[j] = True # Mark as grouped
                    
            output.append(templist)
            
        return output

'''
the underlying logic is right however solution is min n^2 and 
the overall logic isn't fully thre
'''

