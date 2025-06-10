from collections import deque

N, K = map(int, input().split())

arr = []
dq = deque(range(1, N+1))

while dq:
    for _ in range(K - 1):  # K-1명은 뒤로 보냄
        dq.append(dq.popleft())
    arr.append(dq.popleft())  # K번째 사람 제거

print(f"<{', '.join(map(str, arr))}>")

'''
내 코드에서는 불필요한 분기가 있었고, 배열의 길이가 K보다 작아질 때의 처리가 미흡했다.
from collections import deque

N, K = map(int, input().split())

arr = []
dq = deque(range(1, N+1))

while dq:
    for _ in range(K - 1):  # K-1명은 뒤로 보냄
        dq.append(dq.popleft())
    arr.append(dq.popleft())  # K번째 사람 제거

print(f"<{', '.join(map(str, arr))}>")
'''