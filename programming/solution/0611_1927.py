import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if heap:
            print(heapq.heappop(heap))  # 최소값 출력 및 제거
        else:
            print(0)
    else:
        heapq.heappush(heap, cmd)  # 최소 힙에 값 
        
'''
내 코드에서는 sort를 매번 해주어 시간초과가 발생하였음
이런 경우 파이썬 표준 라이브러리인 최소힙을 사용하여 푸는 것이 편하다.

힙이란 우선순위 큐를 구현할 때 사용하는 자료구조로, 항상 가장 큰 값이나 가장 작은 수를 빠르게 꺼낼 수 있는 특수한 트리구조이다
파이썬에서는 heapq라는 표준 라이브러리를 통해 힙 자료구조를 사용할 수 있으며, 기본적으로 최소 힙으로 동작한다.
import heapq
heap = []
-->힙으로 사용할 리스트이기 때문에 초기 선언이 반드시 필요
heapq.heappush(heap,x) 힙에 원소 x를 추가
-->heap 리스트에 x 값을 최소 힙 규칙에 따라 추가
heapq.heappop(heap) 
--> 힙에서 가장 작은 값을 제거하고 반환
heapq.heapify(list) 
-->일반 리스트를 힙 구조로 변환



'''