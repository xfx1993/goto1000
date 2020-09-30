class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        # 时间 O(nk) 空间O(nk)
        n = len(prices)
        if n == 0: return 0
        if k >= n // 2:
            return self.maxProfit0(prices)
        dp = [[[0 for i in range(2)] for j in range(k + 1)] for r in range(n)]
        for i in range(1, k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]

    def maxProfit0(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

        # 如果考虑到第i天的最大收益只与第i - 1天的最大收益相关，空间复杂度可以降低到O(k).
        # 时间O(nk) 空间O(k)
        n = len(prices)
        if n == 0: return 0
        if k >= n // 2:
            return self.maxProfit0(prices)
        dp = [[0 for i in range(2)] for j in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]
        for i in (1, n):
            for j in range(k):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
        return dp[k][0]

    def maxProfit0(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        profit0 = 0
        profit1 = -prices[0]
        for i in range(1, n):
            newProfit0 = max(profit0, profit1 + prices[i])
            newProfit1 = max(profit1, profit0 - prices[i])
            profit0 = newProfit0
            profit1 = newProfit1
        return profit0