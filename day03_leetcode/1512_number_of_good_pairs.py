from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_freqs = defaultdict(int)
        for num in nums:
            num_freqs[num] += 1
        return sum([x * (x - 1) // 2 for x in num_freqs.values()])


def main():
    nums = [int(num) for num in input("Enter numbers: ").split()]
    foo = Solution()
    print("Answer: ", foo.numIdenticalPairs(nums))


if __name__ == "__main__":
    main()
