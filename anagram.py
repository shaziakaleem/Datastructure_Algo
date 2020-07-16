# Solution 1
def check_anagram(a, b):
    d1 = {}
    d2 = {}
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    # remove space and make case sensitive
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    for letter in a:
        if letter in d1:
            d1[letter] = d1[letter] + 1
        else:
            d1[letter] = 1
    for letter in b:
        if letter in d2:
            d1[letter] = d1[letter] + 1
        else:
            d2[letter] = 1
    if d1 == d2:
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")


# Driver code : check_anagram
check_anagram("wedzzsb", "bezdsw")

# Solution 2
def check_anagram2(a, b):
    # remove space and make case sensitive
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    a = sorted(a)
    b = sorted(b)
    if a == b:
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")


# Driver code : check_anagram2
check_anagram2("wh at", "twah")

# Solution 3
def check_anagram3(a, b):
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    l1 = [x for x in a]
    l2 = [x for x in b]
    if len(a) != len(b):
        return "Not AnAGRAM"
    for a in l1:
        if a in l2:
            l2.remove(a)
    if len(l2) == 0:
        return "ANAGRAM"
    else:
        return "NOT ANAGRAM"

# Driver code : check_anagram3
x = check_anagram3("whavt", "twvah")
print(x)
