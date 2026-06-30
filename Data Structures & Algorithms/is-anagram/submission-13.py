class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        """
        mapper = {}
        tracker = {}

        for char in s:
            if char not in mapper:
                mapper[char] = 1
            else:
                mapper[char] += 1

        for char in t:
            if char not in tracker:
                tracker[char] = 1
            else:
                tracker[char] += 1
        
        if mapper == tracker:
            return True
        else:
            return False