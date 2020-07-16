# private method to be started with underscores.


class M(object):
    def public(self):
        print("Public method")

    # private methods start with _
    def _private(self):
        print("private method")


import ctypes
import sys


class DynamicArray(object):
    def __init__(self):
        self.capacity = 1
        self.n = 0
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __get_item__(self, k):
        if not 0 <= k < self.n:
            return IndexError("Out of bound!")

        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.A[self.n] = element
        self.n += 1

    def resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


arr = DynamicArray()
arr.append(1)
print(len(arr), sys.getsizeof(arr))

