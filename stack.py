class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,element):
        self.items.append(element)
    
    def pop(self):
        if len(self.items)==0:
            return "Empty stack..cant pop!"
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def isEmpty(self):
        return self.items == []
    
#driver code
s = Stack()
print("checking if stack is empty ..",s.isEmpty())
s.push(1)
print(s.items)
print("pushing True now ..")
s.push(True)
print(s.items)
s.push(11)
print(s.items)
print("popping --",s.pop())
print(s.items)
print("popping --", s.pop())
print(s.items)
print(s.isEmpty())
print("popping --", s.pop())
print("popping --", s.pop())
print(s.items)
print("checking if stack is empty ..",s.isEmpty())