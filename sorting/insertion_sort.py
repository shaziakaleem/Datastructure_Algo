def insertion_sort(ar):
    for i in range(1,len(ar)):
        current_value = ar[i]
        pos = i
        while pos>0 and ar[pos-1]>current_value:
            ar[pos] = ar[pos-1]
            pos -= 1
        ar[pos] = curre
        nt_value
    print("sorted array",ar)

insertion_sort([2,6,3,9,4,8])
