class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


def main():
    s = input("Enter string: ")
    foo = Solution()
    print("Answer: ", foo.toLowerCase(s))


if __name__ == "__main__":
    main()
