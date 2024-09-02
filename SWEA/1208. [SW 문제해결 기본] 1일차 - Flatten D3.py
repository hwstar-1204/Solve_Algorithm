for tc in range(1, 10+1):
    moves = int(input())
    arr = sorted(list(map(int,input().split())))
    
    for i in range(moves):
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()

    answer = arr[-1] - arr[0]
    print(f"#{tc} {answer}")