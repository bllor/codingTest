'''
1 5 5 5 3 2 1 1 10 2
1 1 10 3 1~10중에 꽃의 종류가 3인 꽃의 개수 -->1개
1 2 7 5 3개
2 3 5  
--> 1 5 0 0 0 2 1 1 10 2
1 1 3 5 --> 1
2 4 7 
--> 1 5 0 0 0 0 0 1 10 2
1 1 10 1 --> 2
'''

arr = '1 2 3 4 5'.split(' ')
print(arr[0:3])
arr[0:3] = ['0']*6
print(arr)
# import sys
# N = int(input())
# arr=[None]*N
# arr = sys.stdin.readline().rstrip().split(' ')
# QN = int(input())
    
# for i in range(QN):
#     Qi = list(map(int, input().split(' ')))
#     if Qi[0]==2:
#         l,r = Qi[1],Qi[2]
#         arr[int(l-1):int(r)] = ['0']*(1+r-l)
#     else:
#         l,r,k = Qi[1],Qi[2],Qi[3]
#         # arr2 = arr[l-1:r-1] 슬라이싱 범위 잘못됨
#         arr2 = arr[l-1:r]
#         print(arr2.count(str(k)))
