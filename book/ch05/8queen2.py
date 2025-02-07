n = 4
m = n * 2 - 1
q = n - 1
pos = [0] * n
flag_a = [False] * n
flag_b = [False] * m
flag_c = [False] * m

num=1
# def put() -> None:
#     for j in range(n):
#         for i in range(n):
#             print('O' if pos[i] == j else 'X', end='')
#         print()
#     print()

def put()->None:
    for i in range(3):
        print(f'{pos[i]:2}',end='')
    print()


def set(i: int) -> None:
    global num
    for j in range(n):
        print(f'set{i} a[{j}] b[{i+j}] c[{i-j+q}] num={num}')
        num+=1
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + q]:
            pos[i] = j
            if i == q:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + q] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + q] = False
    print('--------------------')


set(0)