import sys
N = int(input())
arr=[None]*N
arr = sys.stdin.readline().rstrip().split(' ')
QN = int(input())
    
for i in range(QN):
    Qi = list(map(int, input().split(' ')))
    if Qi[0]==2:
        l,r = Qi[1],Qi[2]
        arr[int(l-1):int(r)] = ['0']*(1+r-l)
    else:
        l,r,k = Qi[1],Qi[2],Qi[3]
        arr2 = arr[l-1:r]
        print(arr2.count(str(k)))