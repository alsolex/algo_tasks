class Solution:
    def numberOfSteps(self, num: int) -> int:
        return bin(num).count("1") * 2 - 1 + bin(num)[2:].count("0")
