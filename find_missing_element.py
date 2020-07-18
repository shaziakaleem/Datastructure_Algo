"""
Given, there are 2 arrays. Find the missing element in one of the array.
a = [1,2,4,6,5,7]
b = [1,7,2,6,5] . In this example 4 is missing"""


# Solution 1
def missing_element(a, b):
    print(a)
    print(b)
    missing_elements = []
    d1 = {}
    d2 = {}
    for num1 in a:
        if num1 in d1:
            d1[num1] += 1
        else:
            d1[num1] = 1
    for num2 in b:
        if num2 in d2:
            d2[num2] += 1
        else:
            d2[num2] = 1
    for key1 in d1.keys():
        if key1 not in d2.keys():
            missing_elements.append(key1)
        elif d1[key1] != d2[key1]:
            missing_elements.append(key1)
    print("missing elements : ", missing_elements)


# Driver code
# missing_element([1, 3, 7, 2, 7], [1, 2, 7])

import collections

# Solution 2 : Using Default Dict
def missing2(a, b):
    missing_elements = []
    d = collections.defaultdict(int)
    for num in a:
        d[num] += 1
    for num in b:
        if not num in d.keys():
            missing_elements.append(num)
        elif d[num] == 0:
            missing_elements.append(num)
        else:
            d[num] -= 1
    return missing_elements

#driver code
x = missing2([1, 2, 5, 6, 7], [1, 2, 3, 8, 6, 3, 7])
print("missing elements :", x)

