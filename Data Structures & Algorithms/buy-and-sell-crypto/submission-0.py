class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                profit1=prices[j]-prices[i]
                profit=max(profit,profit1)
        return profit
        