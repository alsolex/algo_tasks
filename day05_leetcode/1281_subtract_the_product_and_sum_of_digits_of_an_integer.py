class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        digit_prod, digit_sum = 1, 0
        for digit in digits:
            digit = int(digit)
            digit_prod *= digit
            digit_sum += digit
        return digit_prod - digit_sum


def main():
    n = int(input("Enter number: "))
    foo = Solution()
    print("Answer: ", foo.subtractProductAndSum(n))


if __name__ == "__main__":
    main()
