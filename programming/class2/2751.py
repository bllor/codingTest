import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for num in arr:
    print(num)
'''
계수정렬로 풀려고 했으나 내가 작성한 코드는 음수가 아닌 정수일 때 사용할 수 있는 코드임
음수를 고려하지 못하고 풀려고 하니 문제가 풀리지 않아서 답을 확인함
'''
# import sys
# arr=[0]*1000001

# N = int(input())
# for i in range(N):
#     n = int(sys.stdin.readline())
    
#     arr[abs(n)]=1

# print('--------------')
# for i in range(len(arr)):
#     if arr[i] !=0:
#         print(i)
