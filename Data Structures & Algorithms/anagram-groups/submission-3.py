class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # default dictonary with all values to a list
        for string in strs: #for each word in the list
            count = [0]*26 #creates an array of 26 zeros one for each letter
            for char in string: #for each character in the word
                count[ord(char)-ord("a")] += 1 # this is a way to map letters to their positons
            result[tuple(count)].append(string) #append to list in dict
        return list(result.values())  # return the values