""" General Sequential Search. Works on Unordered lists. """
def seq_search(ar,n):
    found=False
    pos = 0
    while pos <len(ar) and not found:
        if ar[pos]==n:
            found=True
            return found
        else:
            pos += 1
    return found

#driver code
arr = [5,6,2,1,8,9]
print (seq_search(arr,11))

"""Sequential search for ordered list"""

def seq_search_ordered(ar,n):
    found=False
    pos = 0
    stopped = False
    while pos <len(ar) and not found and not stopped:
        print(ar[pos])
        if ar[pos]==n:
            found=True
            return found
        elif ar[pos]>n:
            stopped=True
            return found
        else:
            pos += 1
    return found

arr = [5,6,12,21,38,59]
print (seq_search_ordered(arr,11))