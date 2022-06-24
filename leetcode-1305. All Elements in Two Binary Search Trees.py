#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : Given two binary search trees root1 and root2.
#return a list containing all the integers from both trees sorted in ascending order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1 = []
        tree2 = []
        ans = []
        
        def inorder(root, lst):
            if root:
                inorder(root.left, lst)
                lst.append(root.val)
                inorder(root.right, lst)
        
        inorder(root1, tree1)
        inorder(root2, tree2)
        
        i = 0
        j = 0
        while i < len(tree1) and j < len(tree2):
            if tree1[i] == tree2[j]:
                ans.append(tree1[i])
                ans.append(tree2[j])
                i += 1
                j += 1
            elif tree1[i] < tree2[j]:
                ans.append(tree1[i])
                i += 1
            elif tree1[i] > tree2[j]:
                ans.append(tree2[j])
                j += 1
                
        if i < len(tree1):
            for k in range(i, len(tree1)):
                ans.append(tree1[k])
                
        if j < len(tree2):
            for k in range(j, len(tree2)):
                ans.append(tree2[k])
                
        return ans
