class DNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
a = DNode(1)
b = DNode(2)
c = DNode(3)

a.next = b
b.prev = a

b.next = c
c.prev = b


print(b.next.prev.value)