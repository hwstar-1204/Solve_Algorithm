from collections import Counter
T = int(input())
for tc in range(1, T + 1):
# for _ in range(1):
    num = input()
    array = list(map(int,input().split()))

    counter = Counter(array)
    result = counter.most_common()
    result  = sorted(result, key=lambda x: (x[1],x[0]), reverse=True)
    answer = result[0][0]
    print(f"#{num} {answer}") 


