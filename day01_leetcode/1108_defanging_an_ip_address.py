class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


def main():
    foo = Solution()
    address = input("Enter address :")
    print("Answer: ", foo.defangIPaddr(address))


if __name__ == "__main__":
    main()
