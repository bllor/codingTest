import sys
N = int(input())
arr=[None]*N
for i in range(N):
    x,y = map(int, sys.stdin.readline().split(' '))
    arr[i] = [x,y]
# lambda는 익명함수를 만들때 사용하는 함수로 
# lambda x: (x[1],x[0])각 좌표 중에서 y를 먼저보고, x를 본다는 의미이다.
arr.sort(key=lambda x: (x[1],x[0]))
for j in arr:
    print(j[1],j[0])


'''
def add_one(x):
    return x+1

add_one_lambda = lambda x: x+1

print(add_one(5))        # 출력: 6
print(add_one_lambda(5)) # 출력: 6

'''