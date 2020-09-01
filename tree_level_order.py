class BinaryTree:
    def __init__(self,root_val):
        self.key =  root_val
        self.left = None
        self.right =None
    
    def insertLeftChild(self,new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t            
    
    def insertRightChild(self,new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t  

t = BinaryTree(1)
t.insertLeftChild(2)
t.insertRightChild(3)
t.insertLeftChild(4)

import collections

d = collections.deque([1,2,3,5])

def level_order_print(tree):
    if not tree:
        return
    currentCount = 1
    nextCount = 0
    nodes = collections.deque([tree])
    while len(nodes)!=0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print(currentNode.key,end='')
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount==0:
            print()
            currentCount,nextCount = nextCount,currentCount
       

level_order_print(t)                                         