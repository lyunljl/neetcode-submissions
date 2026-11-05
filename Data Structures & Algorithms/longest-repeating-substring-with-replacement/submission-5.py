class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #eduardo
        # sliding window technique keep track of left and right index
        # create dictionary keeping track of characters and counts
        # keep track of window size which is right-left+1
        # main condition is if window size - most frequent <= k keep going
        # replave result with higher value if ever found, return result

        #will hold character and count
        characters = {}
        # current total length
        best_length = 0
        # left pointer
        left = 0

        for right in range(len(s)):
            characters[s[right]]= characters.get(s[right],0) + 1
            while (right-left+1) - max(characters.values()) > k:
                characters[s[left]] -= 1
                left+=1
            best_length = max(best_length,(right-left+1))
            
        
        return best_length

        