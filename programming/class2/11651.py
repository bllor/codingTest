#x,y좌표에서 y를 기준으로 정렬을 해야 하는데 sort()에서 정렬을 변경하는 방법이 생각나지 않아서 x,y를 y,x로 변경한 다음 풀었음
#야매로 풀었으므로 다시 풀어보는 것이 좋을 것 같음
import sys
N = int(input())
arr=[None]*N
for i in range(N):
    x,y = map(int, sys.stdin.readline().split(' '))
    arr[i] = [y,x]
arr.sort()
for j in arr:
    print(j[1],j[0])

