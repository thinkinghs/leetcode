class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        maxprofit = 0
        minprofit = prices[0]
        
        for i in range(len(prices)):
            
            if prices[i] < minprofit:
                minprofit = prices[i]
            elif prices[i] - minprofit > maxprofit:
                maxprofit = prices[i] - minprofit
        return maxprofit
