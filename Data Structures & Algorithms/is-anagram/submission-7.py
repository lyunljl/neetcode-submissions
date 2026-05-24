class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_new = list(s)
            t_new = list(t)
            s_new.sort()
            t_new.sort()
            if s_new == t_new:
                return True
            else:
                return False