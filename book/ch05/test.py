# print(8/22)
# print(22/8)


pos = [0]*3
n = 1
def put()->None:
    for i in range(3):
        print(f'{pos[i]:2}',end='')
    print()

def set(i:int)->None:
    global n  # 전역 변수 사용 선언

    for j in range(3):
        print(f'set[{i}][{j}] {n}번')
        n=n+1
        pos[i]=j
        if i==2:
            put()
        else:
            set(i+1)

set(0)
        