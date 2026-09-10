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
            nonlocal total_average  # Allows modifying the outer variable

            if not node:
                return 0, 0  # Return (sum_of_values, count_of_nodes)

            # Recursively get the sum and count from left and right subtrees
            left_sum, left_count = cyclops(node.left)
            right_sum, right_count = cyclops(node.right)

            # Calculate totals for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1

            # Check if the average matches the node's value
            if current_sum // current_count == node.val:
                total_average += 1

            return current_sum, current_count

        cyclops(root)
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
