import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]
arr = list(map(int, input().split()))

for i, num in enumerate(arr):
  if i>0:
    arr[i] = arr[i-1] + num
print(arr)
for _ in range(m):
  i,j = map(int, input().split())
  print(arr[j] - arr[i-1])

'''
누적합문제
해당 알고리즘에 접근조차 하지 못했음

처음에 접근한 방법은
import sys
N,M = map(int,sys.stdin.readline().rstrip().split(' '))
arr = list(map(int,sys.stdin.readline().rstrip().split(' ')))

# N,M = 5,3
# arr = list(map(int,'5 4 3 2 1'.split(' ')))
# print(sum(arr[0:2]))
p_arr= []
for i in range(M):
    s,t = map(int,sys.stdin.readline().rstrip().split(' '))
    # print(sum(arr[s-1:t]))
    p_arr.append(f'{sum(arr[s-1:t])}')

print('\n'.join(p_arr))
구간을 sum하는 방법이였는데
이 방법의 시간 복잡도는 O(M*N)으로 m과 n이 커질 경우 시간초과가 난다

누적 알고리즘은 값을 저장할 때 누적값으로 저장을 시킨다.
arr = [1,2,3,4,5]일 때
s_Arr = [0,1,3,6,10,15]로 저장이 된다.
1번째 수부터 5번째 수 까지의 합을 구할 경우
s_Arr[5] - s_Arr[1-1] == 15가 나오는 것을 확인할 수 있다.
만약 3번째 수부터 4번째 수까지의 합을 구하는 경우,
arr[4] = 10인데 이는 1번째,2번째 3번째,4번째 수를 더한 값이고,
arr[3-1] = 6인데 이는 1,2번째 수를 더한 값이다
arr[4]-arr[2]는 4,3번째를 더한 값이 된다.


'''