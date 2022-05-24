class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r, res = 0, 0, 0
        for p in s:
            l += p == "("
            r += p == ")"
            if l == r:
                res = max(res, 2 * r)
            elif r > l:
                l = r = 0

        l, r = 0, 0
        for p in s[::-1]:
            l += p == "("
            r += p == ")"
            if l == r:
                res = max(res, 2 * l)
            elif l > r:
                l, r = 0, 0
        return res
