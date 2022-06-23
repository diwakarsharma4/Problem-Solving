#author- diwakar sharma [github- diwakarsharma4]
#-----------------------------------------------

#problem- print all the nodes at the deepest level in a binary tree.
#solution:
#we can use bfs (level order traversal).
#our answer will be the list of nodes at the last level.

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [[]]
        
        def preorder(root):
            if root:
                q = []
                q.append(root)
                
                while q:
                    sublist = []
                    for node in q:
                        sublist.append(node.val)
                    ans[0] = sublist.copy()
                    
                    q_len = len(q)
                    while q_len > 0:
                        node = q.pop(0)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                        q_len -= 1
        preorder(root)
        return ans[0]
      
      
#INPUT: [3,9,20,null,null,15,7]
#OUTPUT: [15,7]
#------------------------------------------------------------------------------
#similar questions:
#find sum/product/average of all nodes at the last level.
