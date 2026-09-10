# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
# We have a recursive function that returns the total no of elements seen, and the total sum of elements
# We will call it on only the beginning, and have the beginning find the others

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total_average = 0
        def cyclops(node):
            nonlocal total_average
            # total, number of elements
            a, b = None, None
            c, d = None, None
            if node.left is not None:
                c, d = cyclops(node.left)
            else:
                c, d = 0, 0
            if node.right is not None:
                a, b = cyclops(node.right)
            else:
                a, b = 0, 0
            total_elements = a + c + 1
            total_no = d + b + node.val
            if total_no // total_elements == node.val:
                total_average += 1
            return total_elements, total_no

        a, b = cyclops(root)
        return total_average

a = TreeNode(4)
b= TreeNode(8)
c = TreeNode(5)
d = TreeNode(0)
e = TreeNode(1)
f = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
sol = Solution()
print(sol.averageOfSubtree(a))
