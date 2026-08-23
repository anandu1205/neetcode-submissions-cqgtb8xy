class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        if n == 1:
            return 0

        dp = [[0] * 2 for _ in range(n)]

        # Day 0
        dp[0][0] = -prices[0]   # Holding
        dp[0][1] = 0            # Allowed to buy

        # Day 1
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(0, -prices[0] + prices[1])

        # Days 2 onwards
        for i in range(2, n):

            # Holding
            dp[i][0] = max(
                dp[i-1][0],
                dp[i-2][1] - prices[i]
            )

            # Not holding / allowed to buy
            dp[i][1] = max(
                dp[i-1][1],
                dp[i-1][0] + prices[i]
            )

        return dp[n-1][1]

        