# 괄호

n = int(input())

for _ in range(n):
    n_list = input()
    stack = []

    for n in n_list:
        if n == '(':
            stack.append(n)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
