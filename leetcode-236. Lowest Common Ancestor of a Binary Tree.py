#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

#solution : 
#The idea is to find path from root to both of the nodes.
#then iterate throgh both of the paths and compare values.
#when a value is not same, means previous node is the LCA for both nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        
        def getpath(root, path, val):
            if not root:
                return False
            
            path.append(root)
                
            if root.val == val:
                return True
                
            if getpath(root.left, path, val) or getpath(root.right, path, val):
                return True
            
            path.pop()
            return False
            
        path1 = []
        path2 = []
        getpath(root, path1, p.val)
        getpath(root, path2, q.val)
        
        if path1 and path2:
            i = 0
            while i < len(path1) and i < len(path2):
                if path1[i].val != path2[i].val:
                    break
                i += 1
            return path1[i-1]
        
            
        
