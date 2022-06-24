#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : You are given two binary trees root1 and root2.

#solution : 
#we will use leb=vel order traversal in both trees simultaniously.
#in case of any child does not have left / right child of one tree while other tree node does have respective left / right child.
#then we will add new node having value 0.
#so that at the time of addition we can easily add values of both the nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None or root2 == None:
            return root1 if root1 else root2
        
        q1 = [root1]
        q2 = [root2]
        
        while q1 and q2:
            curr_node1 = q1.pop(0)
            curr_node2 = q2.pop(0)
            
            if curr_node1 and curr_node2:
                curr_node1.val += curr_node2.val
                
                if not curr_node1.left and curr_node2.left:
                    curr_node1.left = TreeNode(0)
                    
                if not curr_node1.right and curr_node2.right:
                    curr_node1.right = TreeNode(0)
                    
                q1.append(curr_node1.left)
                q1.append(curr_node1.right)
                q2.append(curr_node2.left)
                q2.append(curr_node2.right)
                
            if not curr_node1 and curr_node2:
                curr_node1 = curr_node2
                
        return root1
