
stock_prices = {
    "TCS": 2182,
    "REL": 1297,
    "VEDL": 270,
    "INFY": 1102,
    "JINDALSTEL": 1029
}

portfolio = {}
total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

n = int(input("\nEnter the number of stocks you want to buy: "))

for i in range(n):
    stock = input("\nEnter stock symbol: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n----- Portfolio Summary -----")
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\nTotal Investment Value = ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${investment}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio.txt'")