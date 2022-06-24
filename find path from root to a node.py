#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#Problem : given a root of a binary tree and an integer target.
#find path from root to target, return [] if such path does not exists.

#Solution :
#We will start from the root and recursively keep checking the left and the right child.
#Along with checking we will keep adding the nodes in our answer list.
#In each iteration when we rech to the leaf node and target is not found, we will backtrack and remove all nodes from current wrong path.
#On finding the target node we will add it and return True.

#Tree used :
#                                                           1
#                                                        /     \
#                                                      2         3
#                                                   /     \    /    \
#                                                 4        5  6       7
#                                              /     \   /
#                                             8       9 10
#-------------------------------------------------------------------------------------------------------------------------------------------

#class to create nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#creating binarry tree
def construct_tree(lst, i, n):
    root = None
         
    if i < n:
        root = Node(lst[i])
             
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
             
    return root

#finding path
def path(root, ans, target):
    if root == None:
        return False
    ans.append(root.value)
    if root.value == target:
        return True
    if path(root.left, ans, target) or path(root.right, ans, target):
        return True
    ans.pop()
    return False

 
ans = []
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
target = 4
root = construct_tree(lst, 0, n)
path(root, ans, target)
print(*ans)

#OUTPUT : 1 2 4
