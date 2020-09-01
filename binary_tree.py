class BinaryTree:
    def __init__(self,root_value):
        self.key = root_value
        self.leftChild = None
        self.rightChild = None
    
    def insertleftChild(self,newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRightChild(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRootValue(self):
        return self.key
    
    def setRootValue(self,value):
        self.key = value
    
    def getLeftChild(self):
        return self.leftChild
    
    def getrightChild(self):
        return self.rightChild
    
t = BinaryTree(1)
t.insertleftChild(2)
t.insertRightChild(3)
t.insertleftChild(4)
print(t.leftChild.key)