#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#Problem: You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
#Nodes of a tree are defined as:

#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}

#Solution :
#We will use level order traversal.
#At each level we will iterate through queue and point the right pointer of a node to the next element.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def preorder(root):
            if root:
                q = []
                q.append(root)
                
                while q:
                    q_len = len(q)
                    if q_len>1:
                        for node in range(len(q)-1):
                            q[node].next = q[node+1]
                    
                    while q_len>0:
                        node = q.pop(0)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                        q_len -= 1
        preorder(root)
        return root
