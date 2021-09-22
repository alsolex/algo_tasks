class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_num, jewels = 0, set(jewels)
        for stone in stones:
            if stone in jewels:
                stone_num += 1
        return stone_num


def main():
    foo = Solution()
    jewels = input("Enter jewels string: ")
    stones = input("Enter stones string: ")
    print("answer :", foo.numJewelsInStones(jewels, stones))


if __name__ == "__main__":
    main()
