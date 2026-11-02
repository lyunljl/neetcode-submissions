class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #eduardo
        # create hashmap check if sorted version of item in hashmap, (key, value) -> (sorted, [orginal_strings])
        # if so group the original words in a list
        # edge-case: if string is less than 1 character, not necesary
        output = []
        grouped_words = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in grouped_words:
                grouped_words[sorted_word] = []
                grouped_words[sorted_word].append(word)
            elif sorted_word in grouped_words:
                grouped_words[sorted_word].append(word)

        for group in grouped_words:
            output.append(grouped_words[group])

        return output