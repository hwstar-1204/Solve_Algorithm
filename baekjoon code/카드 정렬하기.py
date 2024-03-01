#카드 정렬하기 
from queue import PriorityQueue

n = int(input())
my_queue = PriorityQueue()
for _ in range(n):
    data = int(input())
    my_queue.put(data)

data1 = 0
data2 = 0
sum = 0
while my_queue.qsize() > 1:
    data1 = my_queue.get()
    data2 = my_queue.get()
    temp = data1 + data2
    sum += temp
    my_queue.put(temp)


print(sum)