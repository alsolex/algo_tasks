from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = dict(zip(indices, s))
        answer = ""
        for i in range(len(indices)):
            answer += shuffled[i]
        return answer


def main():
    s = input("Enter string: ")
    indices = [int(idx) for idx in input("Enter indices: ").split()]
    foo = Solution()
    print("Answer: ", foo.restoreString(s, indices))


if __name__ == "__main__":
    main()
