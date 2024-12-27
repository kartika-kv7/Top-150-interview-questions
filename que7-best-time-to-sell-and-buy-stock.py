class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Set initial min_price to a very high value
        max_profit = 0            # Initialize max_profit to 0
        
        # Loop through the prices array
        for price in prices:
            # Update the min_price
            if price < min_price:
                min_price = price
            # Calculate profit if we sell at current price
            profit = price - min_price
            # Update max_profit if current profit is greater
            if profit > max_profit:
                max_profit = profit
        
        # Return the maximum profit
        return max_profit
