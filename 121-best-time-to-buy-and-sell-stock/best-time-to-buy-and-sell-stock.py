class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # update the minimum price
            else:
                max_profit = max(max_profit, price - min_price)  # calculate profit

        return max_profit
