class Node:
    def __init__(self,value):
        self.value = value
        self.next_node= None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next_node=b
b.next_node=c
c.next_node=d
d.next_node=e

def nth_to_last(n,head):
    left_pointer = head
    right_pointer = head
    for i in range(n):
        if not right_pointer.next_node:
            return 'Error : Out of range'
        right_pointer = right_pointer.next_node
    
    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer


print(nth_to_last(2,a).value)