#반복 과정에서 조건 판단하기
# *를 n개 출력하되 w개마다 줄바꿈을 하는 프로그램

n = 13
w = 3

for i in range(n):
    print('*',end='')
    if i%w==w-1:
        print( )
if n%w:
    print( )