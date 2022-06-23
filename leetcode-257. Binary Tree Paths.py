#author - Diwakar Sharma [github- diwakarsharma4]
#------------------------------------------------

#problem- find path from root node to all the leaf nodes.

#we can use any traversal method inorder/preorder/postorder.
#we will keep adding node values in a list until we don't find a leaf node.
#on reaching leaf node we will add that list in our answer list and then backtrack to pop all the nodes from current path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def inorder(root, sublist):
            if root:
                sublist.append(str(root.val))
                if root.left == None and root.right == None:
                    ans.append((",".join(sublist.copy())).replace(",", "->"))
                inorder(root.left, sublist)
                inorder(root.right, sublist)
                sublist.pop()
                
        ans = []
        inorder(root, [])
        return ans
