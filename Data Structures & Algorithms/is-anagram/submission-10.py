class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)

# sorted() call in Python yeilds a nlogn runtime in the average case