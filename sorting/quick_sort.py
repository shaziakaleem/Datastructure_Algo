'''Quick sort Algorithm'''
def partition(a,start,end):
    pivot = a[start]
    leftmark = start+1
    rightmark = end
    done = False
    while not done:
        while leftmark <= rightmark and a[leftmark]<=pivot:
            leftmark += 1
        while leftmark <= rightmark and a[rightmark]>=pivot:
            rightmark -= 1
        if leftmark>rightmark:
            done = True
        else:
            t = a[leftmark]
            a[leftmark] = a[rightmark]
            a[rightmark] = t
    
    t = a[rightmark]
    a[rightmark] = a[start]
    a[start] = t
    return rightmark


def quick_sort(a,start,end):

    if start<end:
        splitpoint = partition(a,start,end)
        quick_sort(a,start,splitpoint)
        quick_sort(a,splitpoint+1,end)

a = [2,3,1,5,9,4,7]
quick_sort(a,0,len(a)-1)
print(a)