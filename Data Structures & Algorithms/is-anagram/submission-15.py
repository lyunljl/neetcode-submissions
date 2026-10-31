class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #eduardo
        # will convert each string into its own list and sort. Then compare whats in each lists item to see if the same
        if len(s) != len(t):
            return False
        letters_in_s = []
        letters_in_t = []
        for letter in s:
            letters_in_s.append(letter)
        for letter in t:
            letters_in_t.append(letter)

        letters_in_s.sort()
        letters_in_t.sort()
        for i in range(len(letters_in_s)): 
            if letters_in_s[i] != letters_in_t[i]:
                return False
        return True

