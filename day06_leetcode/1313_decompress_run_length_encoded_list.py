from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            decompressed += [nums[i + 1]] * nums[i]
        return decompressed


def main():
    nums = [int(num) for num in input("Enter numbers: ").split()]
    foo = Solution()
    print("Answer: ", foo.decompressRLElist(nums))


if __name__ == "__main__":
    main()
