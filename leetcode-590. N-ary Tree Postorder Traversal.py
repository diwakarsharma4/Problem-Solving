#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def post_order(self, root, ans):
        if not root:
            return
        for node in root.children:
            self.post_order(node, ans)
            
        ans.append(root.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.post_order(root, ans)
        return ans
