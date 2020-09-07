'''Recursive binary search'''
def rec_bin_search(arr,ele):  
    # Base Case
    if len(arr) == 0:
        return False
    # Recursive Case
    else:
        
        mid = int(len(arr)/2)
        if arr[mid]==ele:
            return True
        
        else:    
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            else:
                return rec_bin_search(arr[mid+1:],ele)

ar = [5,6,2,11,8,9]
print (rec_bin_search(ar,1))


def bin_search(arr,ele):
    min = 0
    max = len(arr)
    found = False
    while min<max and not found:
        mid=min+max//2
        if arr[mid] == ele:
            found = True
            return found
        else:
            if ele<arr[mid]:
                max = mid-1
            else:
                min=mid+1
    return found

ar = [5,6,2,11,8,9]
print (bin_search(ar,11))
