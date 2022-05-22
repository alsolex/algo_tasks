class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 1
        for i in range(1, len(s)):
            res += 1
            for j in range(i - 1, -1, -1):
                if s[j : i + 1] == s[j : i + 1][::-1]:
                    res += 1
        return res
