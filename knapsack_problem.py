def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity)] for _ in range(n)]
    for i in range(0, n):
        for w in range(0, capacity):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n - 1][capacity - 1]

weights = [2, 3, 4, 5, 9]
values = [3, 4, 5, 8, 10]
capacity = 10
result = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", result)