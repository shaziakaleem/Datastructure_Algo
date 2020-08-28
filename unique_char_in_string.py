# Problem statement : return true if all characters in a string is unique
''' input : 'abd' returns True
    input : 'afad' returns False
    '''

# 1. Algo solution
def unique_char(s):
    chars = set()
    for c in s:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True
#driver code:
print(unique_char('absa'))

# 2. pythonic way
def check_unique():
    if len(s) == len(set(s)):
        return True
    else:
        return False


# 3. Alternative soln
def is_unique(s):
    if len(s)==0:
        return True
    elif len(s) == 1:
        return True
    ss = sorted(s)
    i = 1
    while i < len(s):
        if ss[i] == ss[i-1]:
            return False
        else:  
            i += 1
    return True
# print(is_unique('abs'))