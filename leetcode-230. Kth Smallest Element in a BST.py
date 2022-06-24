#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#problem : Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

#solution : 
#one of the possible solution is that we use min-heap.
#the idea is to traverse whole tree using any traversal method and push all the elements in min-heap.
#now pop k-1 elements from the heap.
#at the last pop kth element and return it.

from heapq import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def inorder(root):
            if root:
                inorder(root.left)
                heappush(heap, root.val)
                inorder(root.right)
                
        inorder(root)
        
        for i in range(k-1):
            if heap:
                heappop(heap)
        
        if len(heap)>0:
            return heappop(heap)
            
        
        
        
        
