for turn in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    for i in range(2, n-2):
        
        max_left_right = max(*(arr[i-2:i]+arr[i+1:i+3]))
        if arr[i] > max_left_right:
            result += arr[i] - max_left_right

    print(f"#{turn+1} {result}")
