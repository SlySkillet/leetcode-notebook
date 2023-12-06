# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:                                    # BASE CASE
                return [True, 0]                            # [isBalanced, treeHeight]

            left, right = dfs(root.left), dfs(root.right)   # call recursively on left and right
                                                            # creates call stack to search entire depth

            isBalanced = (                                  # creates boolean balanced
                    left[0] and                             # [1] check balance of left
                    right[0] and                            # [2] check balance of right
                    abs(left[1] - right[1]) <= 1            # [3] check height difference within range
                )

            return [isBalanced, 1 + max(left[1], right[1])] # return [isBalanced, treeHeight]
                                                            # 1 is height of root

        return dfs(root)[0]                                 # returns boolean isBalanced
