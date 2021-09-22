from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))
        return max_wealth


def main():
    n = int(input("Enter customer number: "))
    accounts = [[int(n) for n in input().split()] for _ in range(n)]
    foo = Solution()
    print("Answer: ", foo.maximumWealth(accounts))


if __name__ == "__main__":
    main()
