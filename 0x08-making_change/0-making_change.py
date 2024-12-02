#!/usr/bin/python3
def makeChange(coins, total):
    # If the total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    # Base case: 0 coins needed to make 0
    dp[0] = 0
    # Iterate over all possible amounts from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    return dp[total]
