# 543. Diameter of a Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            lft = dfs(root.left)
            rght = dfs(root.right)

            res[0] = max(res[0], 2 + lft + rght)

            return 1 + max(lft, rght)

        dfs(root)
        return res[0]
