class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #eduardo
        # create a list 
        # iterate through the string letter by letter
        # if the current letter matches the final item in the list stop the loop
        # len(list)
        # make a list of substrings
        substring = [[] for i in range(len(s))]
        current_sublist = 0

        # s is empty
        if len(s) == 0:
            return 0

        for i in range(len(s)):
            if s[i] not in substring[current_sublist]:
                substring[current_sublist].append(s[i])
            else:
                duplicate_index = substring[current_sublist].index(s[i])
                current_sublist += 1
                substring[current_sublist] = (substring[current_sublist-1][duplicate_index+1:]) 
                substring[current_sublist].append(s[i])       
        
        return max(len(sub) for sub in substring)