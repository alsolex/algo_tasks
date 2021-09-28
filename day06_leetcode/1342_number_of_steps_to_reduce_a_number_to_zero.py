class Solution:
    def numberOfSteps(self, num: int) -> int:
        op_cnt = 0
        while num != 0:
            op_cnt += 1
            if num % 2 == 1:
                num -= 1
            else:
                num >>= 1
        return op_cnt


def main():
    num = int(input("Enter number: "))
    foo = Solution()
    print("Answer: ", foo.numberOfSteps(num))


if __name__ == "__main__":
    main()
