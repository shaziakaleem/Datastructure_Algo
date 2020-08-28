#problem statement
'''input : 'AAABBCCDDDD'
output : a compressed form : 'A3B2C2D4'
'''


#Run length compression Algorithm : O(n) 
def compression_algo(s):
    i=1
    count = 1
    r = ''
    while i<len(s):
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r+s[i-1]+str(count)
        i += 1
    return r

#driver code
print(compression_algo('AABBCCDDDD'))




# Pythonic way using dictionary
def compress(test_string):
    if len(test_string)==0:
        return ""
    elif len(test_string) == 1:
        return test_string+str(1)
    i=0
    d = {}
    while i < len(test_string):
        if test_string[i] not in d.keys():
            d[test_string[i]] = 1
        else:
            d[test_string[i]] += 1
        i=i+1
    return ''.join([(x+str(d[x])) for x in d])
        

# driver code
print(compress('ABBBBCCDDDD'))
