class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window
        shrink if you know soemthing exists in the set...
        """

        charset = set()
        left = 0
        output = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[r])
            output = max(output, r - left + 1)
        return output