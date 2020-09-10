 
'''Merge sort implementation in python'''
def mergesort(a):
    if len(a)>1:
        mid = int(len(a)/2)
        lefthalf = a[:mid]
        righthalf =a[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                a[k]=lefthalf[i]
                i += 1
            else:
                a[k]=righthalf[j]
                j += 1
            k += 1
        while i<len(lefthalf):
            a[k]=lefthalf[i]
            i +=1
            k +=1
        while j<len(righthalf):
            a[k]=righthalf[j]
            j += 1
            k += 1
        

a = [4,7,5,3,1,8]
mergesort(a)
print(a)