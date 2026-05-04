class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] - buy > profit:
                profit = prices[i] - buy
            buy = min(prices[i], buy) 
        
        return profit

        