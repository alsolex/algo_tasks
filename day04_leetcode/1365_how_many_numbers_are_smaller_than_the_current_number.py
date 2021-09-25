from typing import List

# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dp = [0] * (max(nums) + 1)

        for num in nums:
            dp[num] += 1

        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]

        return [dp[num - 1] if num != 0 else 0 for num in nums]


# the good solution becuase of small values in nums array
# the alternative is sort + binsearch


def main():
    nums = [int(num) for num in input("Enter numbers: ").split()]
    foo = Solution()
    print("Answer: ", foo.smallerNumbersThanCurrent(nums))


if __name__ == "__main__":
    main()
