class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        # Calculate minimum changes for every substring
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for r in range(d):
                        left = i + r
                        right = i + r + (groups - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(2, n + 1):
            for p in range(1, k + 1):
                for j in range(i - 1):
                    if dp[j][p - 1] != INF:
                        dp[i][p] = min(
                            dp[i][p],
                            dp[j][p - 1] + cost[j][i - 1]
                        )

        return dp[n][k]
