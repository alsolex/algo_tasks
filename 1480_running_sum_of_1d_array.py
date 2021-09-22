from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def main():
    foo = Solution()
    nums = [int(num) for num in input("Enter nums: ").split()]
    print("Answer: ", foo.runningSum(nums))


if __name__ == "__main__":
    main()
