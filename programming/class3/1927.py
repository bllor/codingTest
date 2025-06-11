import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    cmd = int(input())
    if cmd==0:
        if not len(arr):
            print(0)
        else:
            print(arr.pop())
    else:
        arr.append(cmd)
    arr.sort(reverse=True)
    # print(arr)

    