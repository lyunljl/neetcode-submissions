class Solution:
    #eduardo
    def encode(self, strs: List[str]) -> str:
        #turn a list of strings into a string
        #use . as a delimiter
        encoded_string = ""
        if len(strs) == 0:
            return ""
        
        for word in strs:
            count = len(word)
            encoded_string += str(count) + "." + word
            
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        #turn original string into list
        decoded_string = []
        current = 0
          
        if len(s) == 0:
            return []

        while current<len(s):
            j=current
            while s[j] != ".":
                j +=1
            length = int(s[current:j])
            #slice exact number of characters after delimiter
            word = s[j+1:j+1+length]
            decoded_string.append(word)

            current = j+1 + length
        return decoded_string
