def get_max_profit(stock_prices_yesterday):
    #This is a dynamic programming question
    matrixSize = len(stock_prices_yesterday)
    #profitMatrix = [[-1 for x in range(len(stock_prices_yesterday))] for y in range(len(stock_prices_yesterday))]
    max_profit = -1 * max(stock_prices_yesterday)
    for x in range(1, len(stock_prices_yesterday)):

        profit = stock_prices_yesterday[x] - min(stock_prices_yesterday[:x])
        if max_profit < profit:
            max_profit = profit

        #for y in range(x+1, len(stock_prices_yesterday)):
        #    profit = stock_prices_yesterday[y] - stock_prices_yesterday[x]
            #profitMatrix[x][y] = profit

    return max_profit

# run your function through some test cases here

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print(get_max_profit(stock_prices_yesterday))
# returns 6 (buying for $5 and selling for $11)

stock_prices_yesterday = [1,2,3,4,5,6,7,8,9,10,11]
print(get_max_profit(stock_prices_yesterday))
# returns 10

stock_prices_yesterday = [11,10,9,8,7,6,5,4,3,2,1]
print(get_max_profit(stock_prices_yesterday))
# returns -1
