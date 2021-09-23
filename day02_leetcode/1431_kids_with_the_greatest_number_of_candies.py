from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        for i in range(len(candies)):
            candies[i] = (candies[i] + extraCandies) >= greatest
        return candies


def main():
    extraCandies = int(input("Enter extraCandies: "))
    candies = [int(num) for num in input("Enter candies: ").split()]
    foo = Solution()
    print("Answer: ", foo.kidsWithCandies(candies, extraCandies))


if __name__ == "__main__":
    main()
