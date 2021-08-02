def maxProfit(prices):

    buy_price = float('inf')
    profit_price = 0

    for val in prices:
        buy_price = min(buy_price, val)
        profit_price = max(val - buy_price, profit_price)

    return profit_price


prices = [7,1,5,3,6,4]
print("Maximum profit = ", maxProfit(prices))