from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums


def main():
    foo = Solution()
    n = int(input("Enter array size: "))
    nums = [int(num) for num in input("Enter array: ").split()]
    print("Answer: ", foo.shuffle(nums, n))


if __name__ == "__main__":
    main()
