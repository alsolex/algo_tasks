class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.hammingWeight(n >> 1) + n % 2 if n > 0 else 0
