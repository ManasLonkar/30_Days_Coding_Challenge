class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Fill the dp array
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, we couldn't make that amount
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
