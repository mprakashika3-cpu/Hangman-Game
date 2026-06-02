# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

stock_name = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment Value =", total)

    file = open("result.txt", "w")
    file.write("Total Investment Value = " + str(total))
    file.close()

    print("Result saved in result.txt")

else:
    print("Stock not found")