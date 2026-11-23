class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        maxP=0
        right = 1

        # for i, price in enumerate(prices):
        while right < len(prices):
            left = 0
            low = sys.maxsize
            while left < right:
                if prices[left]< low: low = prices[left]
                left+=1
            profit = prices[right]-low
            if profit > maxP: maxP = profit
            right +=1

        return maxP

        #10 100 1 2 3 4
        #[10,1,5,6,7,1,8]
        #-9, 4 1 1 -6 7

        #10 8 1 4 3 2
        #-2 -7 3 -1 -1
        #-2 -1 -2 -3