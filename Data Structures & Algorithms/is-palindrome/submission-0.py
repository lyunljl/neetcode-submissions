class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        pointer 1 starts at the front
        pointer 2 starts at the end

        while pointer1 != pointer2
            while pointer1 != pointer2 and isalphanumeric(pointer1)
                pointer1+=1
            while pointer1!= pointer2 and isalphanumeric(pointer2)
                pointer2-=1
        if s[pointer1] == s[pointer2]
            pointer1 += 1
            pointer2 -= 1
        if s[pointer1] != s[pointer2]
            return False
        return True
        '''
        
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
    
        