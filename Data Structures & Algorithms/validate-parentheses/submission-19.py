class Solution:
    def isValid(self, s: str) -> bool:
        #eduardo
        #create stack, this will hold all bracket openings
        #create a dictionary with the matchings
        #collect openings in stack
        #if a close bracket comes up and doesn't match the latest open bracket
        #return false
        #otherwise always return true
        stack_brackets = []
        bracket_pairings = {")":"(", "]":"[", "}":"{"}
        open_brackets= ["(", "[", "{"]

        if len(s) <= 1 or s[0] not in open_brackets:
                return False
        for bracket in s:
            if bracket in open_brackets:
                stack_brackets.append(bracket)
            else:
                if not stack_brackets:
                    return False
                
                if stack_brackets.pop() != bracket_pairings[bracket]:
                    return False
        return len(stack_brackets) == 0

        