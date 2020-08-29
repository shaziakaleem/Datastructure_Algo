''' '(){([[[]]])}'
check if the parenthesis is balanced or not'''

def check_balance(s):
    opening = set('{[(')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            else:
                last_out = stack.pop()
                if (last_out,paren) not in matches:
                    return False
    return len(stack)==0

print(check_balance('(){([[[]]])}'))
