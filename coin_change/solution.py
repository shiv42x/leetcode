class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amnt in range(amount + 1):
            for coin in coins:
                if amnt - coin >= 0:
                    dp[amnt] = min(dp[amnt], 1 + dp[amnt - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1