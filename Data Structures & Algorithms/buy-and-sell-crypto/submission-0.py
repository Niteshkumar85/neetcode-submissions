class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        sell_profit = 0 

        for price in prices:
            if price < buy:
                buy = price

            profit = price - buy

            if profit > sell_profit:
                sell_profit = profit

        return sell_profit
            


            
        