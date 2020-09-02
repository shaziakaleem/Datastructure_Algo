'''
BINARY HEAP
A binary heap is a binary tree with below properties:
1. elements are arranged in level order, first level element from left to right followed by second level
2. value of parent is always smaller than children
3. an additional element 0 is added in binary heap for formula :
    left_child = 2*parent
    right_child = 2*parent+1
4. It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible).
    This property of Binary Heap makes them suitable to be stored in an array.
5. Binary Heap is either Min Heap or Max Heap.
6. A binary heap(complete binary tree) is typically represented as an array.
    '''

class BinHeap:
    def __init__(self):
        self.heap_list =[]
        self.size =0
    
    def percUp(self,i):
        while i//2>0:
            if self.heap_list[i]>self.heap_list[i//2]:
                temp = self.heap_list[i]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = temp
        i = i//2
    
    def add(self,item):
        self.heap_list.append(item)
        self.size += 1
        self.percUp(1)

    def percDown(self,i):
        while i*2> self.size:
            min_child = self.find_min(i)
            if self.heap_list[i]>self.heap_list[min_child]:
                temp = self.heap_list[i]
                self.heap_list[min_child] = self.heap_list[i]
                self.heap_list[i] = temp
    
    def delMin(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size -=1
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist)//2
        self.heap_list = [0]+alist
        self.size = len(alist)
        while(i>0):
            self.percDown(i)
            i -+ 1