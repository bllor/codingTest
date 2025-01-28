# *를 n개 출력하되, w개마다 줄바꿈하기2

n = 13
w = 3

for i in range(n//w):
    print('*'*w)

rest = n%w

if rest:
    print('*'*rest)