
#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#Problem : given a root of a binary tree and two intger node values.
#find path between two nodes, return [] if such path does not exists.

#Solution : 
#we will use root to node path method.
#For on integer at a time we will find path from root to node.
#We will start from the root and recursively keep checking the left and the right child.
#Along with checking we will keep adding the nodes in our answer list.
#In each iteration when we rech to the leaf node and target is not found, we will backtrack and remove all nodes from current wrong path.
#On finding the target node we will add it and return True.
#In both paths the root value is common so we remove that root value from one of them.
#Now we reverse the left path then merge both paths that represents path between two nodes.

#Tree used :
#                                                           1
#                                                        /     \
#                                                      2         3
#                                                   /     \    /    \
#                                                 4        5  6       7
#                                              /     \   /
#                                             8       9 10
#-------------------------------------------------------------------------------------------------

#class to create nodes
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

#finding path fromroot to target
def get_path(root, ans, target):
    if root == None:
        return False
    ans.append(root.value)
    if root.value == target:
        return True
    if get_path(root.left, ans, target) or get_path(root.right, ans, target):
        return True
    ans.pop()
    return False

 
path1 = []
path2 = []
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
get_path(root, path1, 4)
get_path(root, path2, 6)
path1.pop(0)
path1.reverse()
path = path1 + path2
print(*path)

#OUTPUT : 4 2 1 3 6
