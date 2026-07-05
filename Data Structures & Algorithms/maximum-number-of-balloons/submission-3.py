class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        truth = {}

        for char in text:
            if char in 'balon':
                if char not in truth:
                    truth[char] = 1
                else:
                    truth[char] += 1
            else:
                continue
            
        if len(truth) < 5:
            return 0
        
        truth['l'] = truth['l'] // 2
        truth['o'] = truth['o'] // 2 
        #this allows us to ensure the double letters are accounted for

        return min(truth.values()) # the lowest value will be the bottle neck
