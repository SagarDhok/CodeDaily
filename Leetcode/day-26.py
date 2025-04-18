
# "Max Profit: Best Time to Buy and Sell Stock" 📈💰
def maxProfit(): 
    
    prices = [int(i) for i in input("Enter List of stock prices : ").split()]
    min_price = float("inf")
    max_profit = 0
    for val in prices:
        if val < min_price:
            min_price = val
        elif val - min_price > max_profit:
            max_profit = val - min_price
    if max_profit == 0:
        print("No profit can be made from the given stock prices.")
    else:
        print("Maximum profit you can make is: ", max_profit)

maxProfit()

    