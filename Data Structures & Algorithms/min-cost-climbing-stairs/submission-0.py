class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0, 0]
        for i in range(2, len(cost) + 1):
            memo[0], memo[1] = memo[1] , min(memo[0] + cost[i-2], memo[1] + cost[i-1])
        return memo[1]