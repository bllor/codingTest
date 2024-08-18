# 정답코드
n, m = map(int, input().split())

a, b = [], []

for i in range(n):
    i = list(map(int, input().split()))
    a.append(i)

for i in range(n):
    i = list(map(int, input().split()))
    b.append(i)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = " ")
    print()


# 내가 작성한 코드
n,m = map(int, input().split(' '))

ta = []
tb = []
for i in range(n):
    q,w,e = map(int,input().split(' '))
    ta.append([q,w,e])

for i in range(n):
    q,w,e = map(int,input().split(' '))
    tb.append([q,w,e])

for i in range(len(ta)):
    for j in range(len(ta[i])):
        # ta[i][j]=ta[i][j]+tb[i][j]
        print(ta[i][j]+tb[i][j], end=' ')
    print('')
    