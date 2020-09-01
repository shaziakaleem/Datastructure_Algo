def binary_tree(root):
    return [root,[],[]]

def insertleft(newBranch,root):
    t = root.pop(1) # get left child if present
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

def insertRight(newBranch,root):
    t = root.pop(2) # get right child if present
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    

bt = binary_tree(1)
insertleft(2,bt)
insertRight(3,bt)
insertleft(4,bt)
print(bt)