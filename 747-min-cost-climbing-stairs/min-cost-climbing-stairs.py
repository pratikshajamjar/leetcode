from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n  # Initialize dp array of size n

        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Bottom-up DP approach
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # You can reach the top from either of the last two steps
        return min(dp[n - 1], dp[n - 2])
