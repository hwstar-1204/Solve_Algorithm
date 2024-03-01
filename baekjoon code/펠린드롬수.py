#펠린드롬수 
while True:
    n = list(input)
    if n == '0':
        break

    myStack = []
    result = False

    if n%2==1:
        del n[(n//2)+1]

    for i in range(p):
        myStack.append(n[i])
