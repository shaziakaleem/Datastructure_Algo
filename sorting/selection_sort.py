def selection_sort(ar):
    max = ar[0]
    for i in range(len(ar)-1,0,-1):
        for j in range(0,i+1):
            if ar[j]<ar[max]:
                max = j
        t = ar[max]
        ar[max] = ar[i]
        ar[i] = t
    return ar

print(selection_sort([4,23,2,7,21]))