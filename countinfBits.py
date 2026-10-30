class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
# optimal code
# or
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            result.append(bin(i).count('1'))

        return result
