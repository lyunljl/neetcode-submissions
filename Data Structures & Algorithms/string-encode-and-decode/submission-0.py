class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    
    def decode(self, s: str) -> List[str]:
        #  two pointers problem
        # 5#hello5#world10#abcdefghij
        output = []
        pointer1 = 0 # pointer1 starts at the begining

        if len(s) == 0: #random edge case handler
            return output
        
        while pointer1 < len(s): #program only stops when we reach end of list
            # two pointers begins
            pointer2 = pointer1 # pointer1 and pointer 2 meet together
            while s[pointer2] != "#": #keep moving pointer2 until we get a '#'
                pointer2 += 1
            size = int(s[pointer1:pointer2]) #pointer1 to pointer2 now captures the number in string form
            pointer1 = pointer2 + 1 #move pointer1 in front of pointer2 (now the begining of the word)
            pointer2 = pointer1 + size #move pointer 2 the exact length of the word
            output.append(s[pointer1:pointer2]) #sliding window screenshot!!!
            pointer1 = pointer2 #pointers meet back up again
        return output


        

