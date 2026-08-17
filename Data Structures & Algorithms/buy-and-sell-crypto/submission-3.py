class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sys.maxsize
        sell = 0
        profit = 0
        seen = []

        for i in prices:
            if len(seen) > 0:
                buy = min(seen)
            sell = i

            if (sell-buy) > profit: 
                profit = sell-buy

            seen.append(i)
            
        return profit
        