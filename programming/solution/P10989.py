import sys

N  = int(sys.stdin.readline())
arr = [0]*10001 #숫자는 10000보다 작다고 하니 10001을 선언해준다.

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1 # arr[num]에 num이 들어온 개수 count 

for i in range(10001): 
	# arr[i]에 숫자가 들어왔다면 
    if arr[i] != 0:
    	# arr[num]에 num이 들어온 개수 만큼 출력 
        for j in range(arr[i]): 
            print(i)
'''
만약 1,2,1,4가 들어올 경우
arr=[0,2,1,0,4,...]
이렇게 저장이 되는데
1은 2번, 2는 1번, 3은 0번, 4는 1번 출력된다.

'''


'''
메모리 초과로 인해 문제를 풀지 못했음
import sys
N = int(input())

arr=[0]*N <--N이 10000000개 일 경우, 리스트의 크기가 360mb이상이 되므로 메모리 초과가 날 수 있다.

for i in range(N):
    arr[i]=int(sys.stdin.readline())
arr.sort()
# print(arr)
for i in range(N):
    print(arr[i])
'''