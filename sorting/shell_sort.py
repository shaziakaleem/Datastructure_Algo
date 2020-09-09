def shell_sort(a,gap):
    j=gap
    while j<=len(a)-1:
        current_value = a[j]
        pos = j
        for i in range(j-gap,len(a)):
            if pos-gap>=0:
                if a[pos-gap]>current_value:
                    a[pos] = a[pos-gap]
                    pos = pos-gap
                    a[pos]=current_value
                else:
                    break
                i = i-gap
        j += 1


def shell(a):
    gap =int(len(a)/2)
    while gap>=1:
        shell_sort(a,gap)
        gap = int(gap/2)
    return a

print(shell([19,5,17,23,8,21,3,7]))