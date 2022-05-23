class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp, freqs = [[0 for _ in range(n + 1)] for _ in range(m + 1)], {"0": 0, "1": 0}
        for s in strs:
            for l in s:
                freqs[l] += 1
            zeros_num, ones_num = freqs["0"], freqs["1"]

            for i in range(m, zeros_num - 1, -1):
                for j in range(n, ones_num - 1, -1):
                    dp[i][j] = max(1 + dp[i - zeros_num][j - ones_num], dp[i][j])
            freqs = {"0": 0, "1": 0}
        return dp[m][n]
