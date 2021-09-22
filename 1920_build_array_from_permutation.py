from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


def main():
    foo = Solution()
    nums = [int(num) for num in input("Enter numbers: ").split()]
    print("answer :", foo.buildArray(nums))


if __name__ == "__main__":
    main()
