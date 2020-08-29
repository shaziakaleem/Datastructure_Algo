class Queue:
    def __init__(self):
        self.q=[]
    
    def enQ(self,item):
        self.q.insert(0,item)
    
    def deQ(self):
        if len(self.q)==0:
            return "Empty Queue"
        return self.q.pop()
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.q == []

#driver code
Q = Queue()
print("checking if queue is empty ..",Q.isEmpty())
Q.enQ(1)
print(Q.q)
print("Enqueue 11 now ..")
Q.enQ(11)
print(Q.q)
print("popping --",Q.deQ())
print(Q.q)