import sys
import math

input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(N)]
    scores.sort()

    cut = int(round(N * 0.15 + 1e-8))  # 또는 math.floor(N * 0.15 + 0.5)
    trimmed = scores[cut:N - cut]

    avg = sum(trimmed) / len(trimmed)
    print(int(avg + 0.5))  # 일반적인 반올림

'''
round(x.5)일 때는 짝수에 가까운 쪽으로 반올림이 된다
round(2.5)일 때는 2
round(3.5)일 때는 4로 반올림이 되어서 반올림에서 오류가 발생했다.
반올림을 해야하는 경우 math.floor(N * 0.15 + 0.5)를 사용하면 반올림이 제대로 적용이 된다.
그리고
절사평균에서 제외되는 값을 빼고 배열에 넣으려고 아래와 같은 for문을 사용했는데
이 때 시간초과가 난 것 같다.
for i in range(N):
        if i>=except_number and i<=(N-except_number-1):
            arr1.append(arr[i])
            
arr1= arr[except_number:N - except_number]
을 할 경우 쉽게 배열을 만들 수 있다.
N= int(input())
arr = [None]*N
if N==0:
    print(0)
else:
    for i in range(N):
        arr[i] = int(input())
    except_number = round(N*0.15)
    arr.sort()
    arr1 = []

    for i in range(N):
        if i>=except_number and i<=(N-except_number-1):
            arr1.append(arr[i])
    tn =0
    for i in arr1:
        tn+=i
    print(round(tn/len(arr1)))

'''