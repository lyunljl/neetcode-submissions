class Solution:
    def climbStairs(self, n: int) -> int:
        """
        we want to use a memo style dp
        where we can make a memo array of size n
        each spot can be filled with the numbers of ways we can reach said spot,
        each new spot can be calculauted with n - 1 + n - 2
        """

        if n <= 2:
            return n 
            #this is the base case. there is only 2 ways to get to any step less than or equal to 2

        memo = [0] * (n+1)
            #set up said memo table

        memo[1] = 1
        memo[2] = 2

        for i in range(3, n + 1):
            memo[i] = memo[i-1] + memo[i - 2]
            # we only consider the previous 2 elements because we can only take either 1 step or 2 steps at a time
            
        return memo[n]
        