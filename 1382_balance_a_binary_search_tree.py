from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        array_of_node_values = []
        def inorder(node):
            if node is None:
                pass
            else:
                inorder(node.left)
                array_of_node_values.append(node.val)
                inorder(node.right)
        inorder(root)
        def create_tree_from_array(arr):
            if len(arr) == 0:
                return None
            midPoint = len(arr) // 2
            node = TreeNode(arr[midPoint])
            node.left = create_tree_from_array(arr[:midPoint])
            node.right = create_tree_from_array(arr[midPoint+1:])
            return node
        return create_tree_from_array(array_of_node_values)