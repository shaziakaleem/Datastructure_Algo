coins =[2,4,5,10,1]
target = 12
known_target = [0]*(target+1)

def coin_change(target,coins,known_target):
    min_coins=target
    if target in coins:
        known_target[target] = 1
        return 1
    elif known_target[target]>0:
        return known_target[target]
    else:
        for i in [c for c in coins if c<=target]:
            num_coins = 1+coin_change(target-i,coins,known_target)
            print(num_coins)

            if num_coins<min_coins:
                min_coins=num_coins
                known_target[target]=min_coins
        

coin_change(target,coins,known_target)
