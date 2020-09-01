def fib_rec(n):
    out =[]
    cache = [None]*(n+1)
    if n==0 or n==1:
        return n
    if cache[n]!=None:
        return cache
    cache[n] = fib_rec(n-1) + fib_rec(n-2)
    return cache[n]

print(fib_rec(8))