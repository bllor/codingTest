import sys

N = int(input())
stack = []
for i in range(N):
    i_value = sys.stdin.readline()
    if 'push' in i_value:
        cmd,number = i_value.split(' ')
        stack.append(int(number))
    elif 'pop' in i_value:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in i_value:
        print(len(stack))
    elif 'empty' in i_value:
        if len(stack):
            print(0)
        else:
            print(1)
    elif 'top' in i_value:
        if len(stack):
            print(stack[len(stack)-1])
        else:
            print(-1)
