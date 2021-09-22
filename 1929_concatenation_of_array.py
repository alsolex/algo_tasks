from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums


def main():
    foo = Solution()
    nums = [int(num) for num in input("Enter numbers: ").split()]
    print("answer : ", foo.getConcatenation(nums))


if __name__ == "__main__":
    main()
