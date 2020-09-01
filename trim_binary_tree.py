from binary_tree import BinaryTree

t = BinaryTree(1)
t.insertleftChild(12)
t.insertRightChild(3)
t.insertleftChild(4)

def tree_traversal_inorder(tree):
    if tree:
        print(tree.key,"  ",end='')
        tree_traversal_inorder(tree.leftChild)
        tree_traversal_inorder(tree.rightChild)

def trim_bst(tree, min_val,max_val):
    #post order : left-right-root
    if not tree:
        return
    tree.left = trim_bst(tree.leftChild,min_val,max_val)
    tree.right = trim_bst(tree.rightChild,min_val,max_val)
    if tree.key>=min_val and tree.key<=max_val:
        return tree
    if tree.key<min_val:
        return tree.rightChild
    if tree.key>max_val:
        return tree.leftChild


tree_traversal_inorder(t)
trimmed_BinarySearchTree = trim_bst(t,3,5)
print()
tree_traversal_inorder(trimmed_BinarySearchTree)