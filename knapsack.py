def knapsack(bags, profits, maxWeight):
    items = len(bags)
    dp = [[0] * (maxWeight + 1) for _ in range(items + 1)]
    for i in range(1, items + 1):
        for cap in range(1, maxWeight + 1):
            if bags[i-1] <= cap:
                dp[i][cap] = max(profits[i-1] + dp[i-1][cap - bags[i-1]], dp[i-1][cap])
            else:
                dp[i][cap] = dp[i-1][cap]
    return dp[items][maxWeight]

weights = [2, 4, 6]
values = [3, 5, 8]
capacity = 8
print(knapsack(weights, values, capacity))
