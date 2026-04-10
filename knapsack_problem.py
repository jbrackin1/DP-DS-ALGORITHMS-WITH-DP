def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]  # +1 for including capacity = 0

    # Fill the DP table
    for i in range(1, n + 1):  # Start from 1 to n (instead of 0 to n)
        for w in range(1, capacity + 1):  # Start from 1 to capacity
            if weights[i - 1] <= w:  # Can we include this item in the knapsack?
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])  # Include or exclude the item
            else:
                dp[i][w] = dp[i - 1][w]  # Can't include the item, so just carry forward the previous value

    return dp[n][capacity] 

weights = [2, 3, 4, 5, 9]
values = [3, 4, 5, 8, 10]
capacity = 10

print(knapsack(weights, values, capacity))