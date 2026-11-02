class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
            
        memo = [1, 2]

        for i in range(3, n + 1):
            memo[0], memo[1] = memo[1], (memo[0] + memo[1])
        
        return memo[1]