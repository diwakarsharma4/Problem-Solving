#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : Given the root of a binary tree, return the leftmost value in the last row of the tree.

#solution :
#we will simply use level order traversal and find list of last level node values.
#then return first element of this list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def preorder(root, last_level):
            if root:
                q = []
                q.append(root)
                while q:
                    sublist = []
                    for node in q:
                        sublist.append(node.val)
                    self.last_level = sublist.copy()
                    q_len = len(q)
                    
                    while q_len > 0:
                        node = q.pop(0)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                        q_len -= 1
                        
        self.last_level = []
        preorder(root, self.last_level)
        return self.last_level[0]
