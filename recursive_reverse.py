def rev(s):
    if len(s)==1:
        return s
    else:
        return rev(s[1:])+ s[0] #or return s[len(s)-1] + rev(s[:len(s)-1])
print(rev('hello world'))
