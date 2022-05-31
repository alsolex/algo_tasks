class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_combs_num = 2 ** k
        if all_combs_num > len(s) - k + 1:
            return False
        combs = set()
        for i in range(len(s) - k + 1):
            combs.add(s[i : i + k])
            n = len(combs)
            if all_combs_num - n > len(s) - i - k + 1:
                return False
            if n == all_combs_num:
                return True
        return False
