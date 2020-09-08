def bubble_sort(ar):
    for i in range(len(ar)-1,0,-1):
        for j in range(i):
             if ar[j]>ar[j+1]:
            #swap
                t = ar[j]
                ar[j] = ar[j+1]
                ar[j+1] = t
    return ar

print(bubble_sort([4,2,7,1,9,33,32,15,21]))