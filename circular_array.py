"""circular array
-push : end of array
-pop : removed from the top
"""

import array as arr

len_arr = 8
a = [None] * 8

def circlular(a, index):
    limit = index
    if index <= len(a) - 1:
        while index < len(a):
            print(a[index])
            index += 1
    if index > len(a) - 1:
        index = len(a) - index
        while index < limit:
            print(a[index])
            index += 1


# Driver Code
a = [1,2,3,4,5,6,7,8]
circlular(a, 3)