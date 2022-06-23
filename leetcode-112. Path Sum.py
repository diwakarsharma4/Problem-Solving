#author- Diwakar Sharma [github- diwakarsharma4]
#-----------------------------------------------

#problem- given a root of a binary tree and an integer k.
#find whether a path exist FROM ROOT TO LEAF such that adding up all the values along the path equals to k.

#solution:
#we can use any tree traversal method.
#just on extra thing is that when ever we reach at the leaf node and path sum is not equal to k.
#then we will perform backtrack by subtracting all node values from the current path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def inorder(root, path_sum, flag):
            if root:
                path_sum += root.val
                if not root.left and not root.right:
                    if path_sum == targetSum:
                        self.flag = True
                inorder(root.left, path_sum, self.flag)
                inorder(root.right, path_sum, self.flag)
                path_sum -= root.val
                
        path_sum = 0  
        self.flag = False
        inorder(root, path_sum, self.flag)
        return self.flag
      
      
      
#INPUT: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#OUTPUT: true
