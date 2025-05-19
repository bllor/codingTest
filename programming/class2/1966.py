import sys
tn = 1
for i in range(tn):
    n,m = 6,0
    i_arr = list(map(int, sys.stdin.readline().split(' ')))
    # print(i_arr)
    qq = [None]*n
    for j in range(n):
        qq[j] = [i_arr[j],j]
    print(qq)
    qq.sort(reverse=True)
    print(qq)    