class Node:
    def __init__(self,value):
        self.value = value
        self.next_node= None

a = Node(1)
b = Node(2)
c = Node(3)
a.next_node=b
b.next_node=a

print(a.next_node.value)

def cycle_check(node):
    marker1 = node
    marker2 = node
    while marker2!= None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node
        if marker1 == marker2:
            return True
    return False

print(cycle_check(a))