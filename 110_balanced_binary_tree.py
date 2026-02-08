from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node):
            if node is None:
                return 0  # height of empty tree

            left = check(node.left)
            if left == -1:
                return -1  # left subtree already unbalanced

            right = check(node.right)
            if right == -1:
                return -1  # right subtree already unbalanced

            if abs(left - right) > 1:
                return -1  # current node unbalanced

            return max(left, right) + 1  # return height

        return check(root) != -1
