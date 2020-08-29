class Node:
    def __init__(self,value):
        self.value = value
        self.next_node= None

a = Node(1)
b = Node(2)
c = Node(3)
a.next_node=b
b.next_node=c
print("Initially : ",b.next_node.value)

def reversal(head):
    prev_node = None
    current = head
    next_node = None

    while current:
        next_node = current.next_node
        current.next_node =  prev_node

        prev_node = current
        current = next_node
    return prev_node

reversal(a)   
print("After reversal : ",b.next_node.value)
