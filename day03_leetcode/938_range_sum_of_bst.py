from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val >= low and root.val <= high:
            return (
                self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
                + root.val
            )
        elif root.val > low:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < high:
            return self.rangeSumBST(root.right, low, high)
        return 0


### TODO reading tree procedure
def main():
    pass
    # foo = Solution()
    # print("Answer: ", foo.rangeSumBST(tree))


if __name__ == "__main__":
    main()
