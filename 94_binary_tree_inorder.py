class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        else:
            res1 = self.inorderTraversal(root.left)
            if len(res1) < 1:
                print("Left is empty")
                pass
            else:
                print("Left is not empty")
                res1.extend(res1)
            result.append(root.val)
            res2 = self.inorderTraversal(root.right)
            if len(res2) < 1:
                print("Right is empty")
                pass
            else:
                print("Right is not empty")
                res2.extend(res2)
            return result
