import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]
arr += list(map(int, input().split()))

for i, num in enumerate(arr):
  if i>0:
    arr[i] = arr[i-1] + num

for _ in range(m):
  i,j = map(int, input().split())
  print(arr[j] - arr[i-1])

'''
누적합문제
해당 알고리즘에 접근조차 하지 못했음

'''