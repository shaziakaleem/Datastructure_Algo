"""
Find array pairs
input : [1,3,2,2],4
output : (1,3),(2,2)"""

def check_pair(a, sum):
    if len(a) <= 2:
        return "invalid input"
    seen = set()
    output = set()
    for num in a:
        target = sum - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return output

#Driver code
x = check_pair([1, 3, 2, 2], 4)
print(x)
