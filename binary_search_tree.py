class TreeNode:
    def __init__(self,key,payload='',left=None,right=None,parent=None):
        self.key=key
        self.payload = payload
        self.left = left
        self.right = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.left

    def hasrightChild(self):
        return self.right
    
    def haschildren(self):
        return self.left pr self.right
    
    def hasBothChildren(self):
        return self.left and self.right
    
    def isleft(self,node):
        return self.parent.left = self
    
    def isright(self,node):
        return self.parent.right = self

    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return self.left==None and self.right ==None
    
    def changeNodeValue(self,key,payload,left,right):
        self.key=key
        self.payload = payload
        self.left = left
        self.right = right
        self.parent = parent
        if self.hasLeftChild():
            self.left.parent=self
        if self.hasrightChild():
            self.right.parent = self
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size =0
    
    def put(self,key):
        if not self.root:
            self.root = TreeNode(key)
            self.size += 1
        else:
            self._put(self,key,self.root)

    def _put(self,key,val,currentNode):    
        if key>currentNode.key:
            if currentNode.hasrightChild():
                self._put(key,self.root.right)
            else:
                currentNode.right = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasLeftChild:
                self._put(key,self.root.left)
            else:
                currentNode.left = TreeNode(key,val,parent=currentNode)

    def traverse(self,tree):
        if not self.root:
            return
        l1 = []
        #inorder
        traverse(self.root.left)
        l1.append(self.root.key)
        traverse(self.root.right)

    def __iter__(self):
        if self.left:
            for elem in self.left:
                yield elem
        yield self.key
        if self.right:
            for elem in self.right:
                yield elem

    def get(self,key):
        if not self.root:
            return
        else:
            self._get(key,self.root)

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        if key==currentNode.key:
            return currentNode
        elif key<currentNode.key:
            self._get(key,currentNode.left)
        else:
            self._get(key,currentNode.right)
    
    def delete(self,key):
        if not self.root:
            return
        else:
            self._delete(key)
    
    def find_predecessor(self,node):
        if node.hasLeftChild():
            while node!=None:
                pred = node.right
            return pred
        else:
            return None
    
    def find_successor(self,node):
        if node.hasrightChild():
            while node!=None:
                successor = node.left
            return successor

        else:
            return None

    def splice_out(self,node):
        #we can only splice node with no or one child
        if node.isLeaf():
            if node.isleft(): #check if NODE is a left child
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left: #node is left child check
            if node.left.isleft():
                node.left.parent = node.parent
                node.parent.left = node.left
            else:
                node.right.parent = node.parent
                node.parent.right = node.right
        else:
            if node.isleft():
                node.parent.left = node.right
                node.right.parent = node.parent
            else:
                node.right.parent = node.parent
                node.parent.right = node.right


    def _delete(self,key,currentNode):
        if not currentNode:
            return None
        else:
            if key == currentNode.key:
                #case 1: leafnode
                if not currentNode.haschildren(): 
                    parent = currentNode.parent
                    parent.left = parent.right = None
                #case 2(i) : One child - only left child present
                elif not currentNode.right: 
                    currentNode.key = currentNode.left.key 
                    currentNode.left = None
                #case 2(ii): One child - only right child present
                elif not currentNode.left: 
                    currentNode.key = currentNode.right.key 
                    currentNode.right = None
                #case 4 : both children
                else: 
                    successor = self.find_successor(currentNode) #find successor-replace with successor
                    currentNode.key = successor.key #copy successor to current
                    currentNode.left = self._delete(key,currentNode.right) #delete successor
            elif key<currentNode.key:
                self._delete(key,currentNode.left)
            else:
                self.delete(key,currentNode.right)
