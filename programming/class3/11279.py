import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    cmd = int(input())
    if cmd ==0:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -cmd)