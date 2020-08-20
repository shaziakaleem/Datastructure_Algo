def get_sum(ar):
    if len(ar)==0:
        return "Invalid input"
    
    current_sum = max_sum = ar[0]
    for num in ar[1:]:
        print("max(",current_sum+num,",",num,")")
        current_sum = max(current_sum+num,num)
        print("current_sum = ",current_sum)

        max_sum = max(current_sum,max_sum)
        print("max_sum = ",max_sum)
    return max_sum


#driver code
a = [1,2,-1,3,4,10,10,-10,-1]
get_sum(a)
