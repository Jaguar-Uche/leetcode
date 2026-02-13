from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return []
        else:
            res.append(root.val)
            res1 = self.preorderTraversal(root.left)
            if len(res1) >= 1:
                res.extend(res1)
            res2 = self.preorderTraversal(root.right)
            if len(res2) >= 1:
                res.extend(res2)
        return res