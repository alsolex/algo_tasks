# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        return self.checkVal(cloned, target)

    def checkVal(self, root, target):
        if root:
            if root.val == target.val:
                return root
            left_subtree_res = self.checkVal(root.left, target)
            right_subtree_res = self.checkVal(root.right, target)
            if left_subtree_res:
                return left_subtree_res
            if right_subtree_res:
                return right_subtree_res
        return None
