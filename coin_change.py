def fewest_coins(coins, target):
    limit = target + 1
    dp = [limit] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for amt in range(coin, target + 1):
            if dp[amt - coin] + 1 < dp[amt]:
                dp[amt] = dp[amt - coin] + 1
    return dp[target] if dp[target] != limit else -1

available_coins = [1, 3, 4]
required_sum = 6
print(fewest_coins(available_coins, required_sum))
