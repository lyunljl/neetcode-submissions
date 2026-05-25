class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        we can build a dict that mapps Char count to list with words
        since anagrams sorted are equal. we can iterate through each string and sort it
        after that we can add the sorted thring to dictionary
        sorted string maps to a list
        since dicts can't have dupes. if a sorted word "s" already exists in dict. we can append it to the list in its values
        if not defaultdict will create a new key-value pair and continue
        return the values of the dict asa list
        '''

        results = {}

        for string in strs:

                
            sorted_string = "".join(sorted(string))

            if sorted_string not in results:
                results[sorted_string] = []

            results[sorted_string].append(string)
            
        return list(results.values())