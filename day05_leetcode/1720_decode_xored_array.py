from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        reconstructed = [first]
        for cur_num in encoded:
            reconstructed.append(reconstructed[-1] ^ cur_num)
        return reconstructed


def main():
    first = int(input("Enter first element: "))
    encoded = [int(num) for num in input("Enter encoded arr: ").split()]
    foo = Solution()
    print("Answer: ", foo.decode(encoded, first))


if __name__ == "__main__":
    main()
