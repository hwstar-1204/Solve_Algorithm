stack = list(input())
idx = len(stack)-1
result = 0

while idx != -1:
    print(stack[idx], result)

    n = stack[idx]
    if n == ')':
        idx -= 1
    elif n == '(':
        result *= int(stack[idx-1])
        idx -= 2
    else:
        result += 1
        idx -= 1
    
    

print(result)


# 11 (1 8( 72 (7 )) )

# 11(18(72(7)))

assert stack[-1] == ')'