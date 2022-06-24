#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : given a root of a binary tree find maximum depth of a tree.

#solution :
#The idea is to use any traversal method, here we are using inorder traversal.
#and maintain a counter variable.
#update counter variable with the values returned by all recursive calls.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        def inorder(root, count):
            if root:
                return max(inorder(root.left, count+1), inorder(root.right, count+1))
            else:
                return count
            
        ans = inorder(root, count)
        return ans
      
#-------------------------------------------------------------------------------------------------      

#Find minimum depth of a binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root==None:
                return 0
            if root.left == None or root.right == None:
                return max(inorder(root.left), inorder(root.right)) + 1
            else:
                return min(inorder(root.left), inorder(root.right)) + 1
        ans = inorder(root)
        return ans
      
      
#--------------------------------------------------------------------------------------------------

#Find maximum depth of an N-ary tree.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        depth = 0
        for node in root.children:
            depth = max(depth, self.maxDepth(node))
            
        return depth + 1
