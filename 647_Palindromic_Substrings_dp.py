class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        pals_cnt = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i < 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                pals_cnt += dp[i][j]
        return pals_cnt
