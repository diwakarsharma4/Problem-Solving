#author - Diwakar Sharma [github- diwakarsharma4]
#------------------------------------------------

#problem- Insert an element into a Binary Search Tree.

#To add an element in a BST we will simply use the recursive BST construction method.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def add_node(root, val):
            if root:
                if val < root.val:
                    if root.left == None:
                        root.left = TreeNode(val)
                    else:
                        add_node(root.left, val)
                elif val > root.val:
                    if root.right == None:
                        root.right = TreeNode(val)
                    else:
                        add_node(root.right, val)
            else:
                root = TreeNode(val)
                return root
            
        return add_node(root, val) if add_node(root, val) else root
                    
