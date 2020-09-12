from string import ascii_lowercase

def word_ladder(beginword,endword,wordlist):
    if endword not in wordlist or beginword not in wordlist:
        return 0
    q = []
    visited = set()
    q.append(beginword)
    visited.add(beginword)
    changes = 1
    while q is not None:
        size = len(q)
        for i in range(size):
            currentword = q.pop()
            if currentword==endword:
                return changes
            for j in range(len(currentword)):
                for k in ascii_lowercase:
                    nw = currentword[:j]+k+currentword[j+1:]
                    if nw in wordlist and nw not in visited:
                        visited.add(nw)
                        q.append(nw)
            changes += 1
        print("Visit : ",visited)
    return changes 

wordlist =['hit','hot','dog','lot','cog','dot','log']
print(word_ladder('hit','hot',wordlist))