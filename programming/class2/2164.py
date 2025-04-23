'''
1,2,3,4
2 3 4 -> 3 4 2
4 2 -> 2 4
4

123456
23456 -> 34562
4562 -> 5624
624 -> 246
46 -> 64
4

1234567
0234567 0345672
45672 56724
6724 7246
246 462
62 26
6
'''
# arr = [1,2,3,4]
# arr.remove(arr[0])
# print(arr)
# arr.append(2)
# print(arr)

from collections import deque
import sys
# 큐 생성
queue = deque()
N = int(sys.stdin.readline())
for i in range(1,N+1):
    queue.append(i)
# print(queue)

while True:
    rn = queue.popleft()
    if len(queue)==1:
        break
    bn = queue.popleft()
    queue.append(bn)

print(queue.popleft())
        
    

# while len(arr)==1:
#     N = int(input())
#     arr= [None]*N
#     for i in range(1,N+1):
            
