# recursive approach

fibo_list = [0, 1]


def fibonacci_no(limit):
    global fibo_list
    if limit <= 0:
        return 0
    elif limit == 1:
        return 0
    elif limit == 2:
        return 1
    else:
        x = fibonacci_no(limit - 1) + fibonacci_no(limit - 2)
        if limit > len(fibo_list):
            fibo_list.append(x)
        return x


result = fibonacci_no(8)
print(fibo_list)
