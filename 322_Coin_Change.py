import numpy as np


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp, coins = np.zeros(amount + 1).astype(int) - 1, np.asarray(coins)
        dp[0] = 0
        for i in range(1, len(dp)):
            relev_cases = dp[i - coins[coins <= i]]
            valid_cases = relev_cases[relev_cases != -1]
            if len(valid_cases) > 0:
                dp[i] = min(valid_cases) + 1
        return dp[-1] if dp[-1] > 0 else -1
