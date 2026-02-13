from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def traverse(node):
    res = []
    if node is None:
        return None
    else:
        res.append(node.val)
        res1 =traverse(node.left)
        if res1 is not None:
            res.extend(res1)
        res2 = traverse(node.right)
        if res2 is not None:
            res.extend(res2)
    return res
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = traverse(p)
        res2 = traverse(q)
        if res1 == res2:
            return True
        else:
            return False
