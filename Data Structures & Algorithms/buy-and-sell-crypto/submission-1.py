class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        profit = 0
        if len(prices) < 2:
            return 0
        while rp < len(prices):
            if prices[rp] > prices[lp]:
                temp = prices[rp] - prices[lp]
                profit = max(temp, profit)
            else:
                lp = rp
            rp += 1
        return profit
        
