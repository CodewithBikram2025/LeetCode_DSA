class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_price_to_buy = prices[0]
        
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - best_price_to_buy)
            best_price_to_buy = min(best_price_to_buy, prices[i])

        return profit