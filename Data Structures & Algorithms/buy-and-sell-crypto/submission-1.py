class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = sys.maxsize
        maxP=0
        for price in prices:
            if price < low: low = price
            profit = price - low 
            maxP=max(maxP, profit)

        return maxP