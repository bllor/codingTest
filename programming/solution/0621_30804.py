import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

count = {}  # 숫자 등장 횟수를 저장
start = 0
max_length = 0

for end in range(N):
    num = arr[end]
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    # 숫자 종류가 2개 초과하면 왼쪽 포인터 이동
    while len(count) > 2:
        left_num = arr[start]
        count[left_num] -= 1
        if count[left_num] == 0:
            del count[left_num]
        start += 1

    max_length = max(max_length, end - start + 1)

print(max_length)


'''
내 코드는 시간 초과가 발생함
이 문제는 서로 다른 숫자가 2개 이하인 가장 긴 연속 부분 수열의 길이를 구하는 문제이다.
나는 모든구간을 일일이 비교하는 완전탐색 방식을 사용했는데 이는 시간초과가 발생한다.
이 문제는 투포인터 기법을 사용하여 풀어야 한다.
* 투포인터란 두개의 포인터(인덱스)를 사용하여 배열이나 문자열을 효율적으로 탐색하는 기법을 말한다.

N = 5
arr = '5 1 1 2 1'
count = {}
start = 0
max_length = 0
for end in range(N):
    num = 5
    if num in count:
        count[num] +=1
    else:
        count[num] = 1
    --> count {5:1}
    
    while len(count)>2: #count의 길이가 2를 초과할 때만 while이 실행된다.
        left = arr[start]
        count[5]-=1
        if count[left]==0:
            del count[left]
        start+=1
    max_length = max(max_length,end-start+1)


import sys
N = int(input())
value= sys.stdin.readline().rstrip()
arr = value.split(' ')
maxLength = 1

for i in range(len(arr)):
    i_arr = set()
    i_arr.add(arr[i])
    mm=1
    for j in range(i+1,N):
        i_arr.add(arr[j])
        # print(i_arr,mm)
        if len(i_arr)>2:
            if mm>maxLength:
                # print(mm,maxLength)
                maxLength=mm
            mm=1
            break
        mm+=1
    if mm>maxLength:
        # print(mm,maxLength)
        maxLength=mm
print(maxLength)

'''