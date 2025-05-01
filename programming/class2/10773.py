from collections import deque

N = int(input())

dq = deque()
# print(dq)
for i in range(N):
    iv = int(input())
    if iv ==0:
        dq.pop()
    else:
        dq.append(iv)
print(sum(dq))