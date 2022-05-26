class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res, max_length, counter = 0, 0, 0
        for b in s:
            counter = counter + 1 if b == "(" else counter - 1
            if counter < 0:
                counter, max_length = 0, 0
            else:
                max_length += 1
                if counter == 0:
                    res = max(res, max_length)

        counter, max_length = 0, 0
        for b in s[::-1]:
            counter = counter + 1 if b == ")" else counter - 1
            if counter < 0:
                counter, max_length = 0, 0
            else:
                max_length += 1
                if counter == 0:
                    res = max(res, max_length)
        return res
