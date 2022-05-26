class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        nums = sorted(envelopes, key=lambda x: [x[0], -x[1]])
        max_val = 10 ** 5 + 1
        dp = [max_val] * (len(nums) + 1)
        for elem in nums:
            dp[bisect_left(dp, elem[1])] = elem[1]
        return dp.index(max_val)
