class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #1 1 1 1 1 1 1 
        #1 2 0 0 0 0 0 
        #1 3 0 0 0 0 0
        dp = [[0] * n for _ in range(m)]

        for col in range(n):
            dp[0][col] = 1
        for row in range(m):
            dp[row][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] += dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]               
