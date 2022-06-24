#author- Diwakar Sharma [github- diwakarsharma4]
#-----------------------------------------------

#Problem : given a root of a binary tree, print left / right view of tree.

#Tree used :
#                                                           1
#                                                        /     \
#                                                      2         3
#                                                   /     \    /    \
#                                                 4        5  6       7
#                                              /     \   /
#                                             8       9 10
#-------------------------------------------------------------------------------------------------

#Left view :

#class to create node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#creating binary tree
def construct_tree(lst, i, n):
    root = None
         
    if i < n:
        root = Node(lst[i])
             
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
             
    return root

  
#left view of a tree
def left_view(root, level, maxlevel):
    if root:
        if maxlevel[0]<level:
            ans.append(root.value)
            maxlevel[0] = level
        left_view(root.left, level+1, maxlevel)
        left_view(root.right, level+1, maxlevel)
    return ans
     
     
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
ans = []
view = left_view(root, 1, [0])
print(*view)

#OUTPUT: 1 2 4 8
#------------------------------------------------------------------------------------------------

#Right view :

#class to create node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#creating binary tree
def construct_tree(lst, i, n):
    root = None
         
    if i < n:
        root = Node(lst[i])
             
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
             
    return root

  
#right view of a tree
def right_view(root, level, maxlevel):
    if root:
        if maxlevel[0]<level:
            ans.append(root.value)
            maxlevel[0] = level
        right_view(root.left, level+1, maxlevel)
        right_view(root.right, level+1, maxlevel)
    return ans
     
     
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
ans = []
view = right_view(root, 1, [0])
print(*view)

#OUTPUT: 1 3 7 10
#----------------------------------------------------------------------------------------------------------
