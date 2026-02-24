# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_tree(root):
    paths = []

    def dfs(node, path):
        if not node:
            return

        # extend current path with this node
        path = path + str(node.val)

        # if leaf → store path
        if not node.left and not node.right:
            paths.append(path)
            return

        # continue traversal
        dfs(node.left, path)
        dfs(node.right, path)

    dfs(root, "")
    return paths

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        arr = traverse_tree(root)
        print(arr)
        total = 0
        for bin_str in arr:
            if bin_str != '':
                total += int(bin_str, 2)
        return total

t = TreeNode(1)
k = TreeNode(0)
l = TreeNode(1)
m = TreeNode(0)
n = TreeNode(1)
o = TreeNode(0)
p = TreeNode(1)
t.left = k
t.right = l
k.left = m
k.right = n
l.left = o
l.right = p
solution = Solution()
print(solution.sumRootToLeaf(t))
# print(traverse_tree(t))
# s = ""
# a = int(s, 2)
# a = bin(int(s))
# print(a)
# a = TreeNode(1)
# print(traverse_tree(a))
