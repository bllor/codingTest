from collections import deque
N,K = map(int,input().split(' '))
# N,K = 7,3

arr = []
dq = deque([i for i in range(1,N+1)])

while len(dq):
    if len(dq)==1:
        arr.append(dq.popleft())

    if len(dq)<K:
        K = len(dq)%(K-1)
    # print('K',K)    
    for i in range(len(dq)):
        # print(i)
        if i==K and K==0:
            r1 = dq.popleft()
            arr.append(r1)
        if i<K-1:
            r1 = dq.popleft()
            dq.append(r1)
        if i==K-1:
            r1 = dq.popleft()
            arr.append(r1)
# print(arr)
print(f"<{', '.join(map(str, arr))}>")