import sys
input = sys.stdin.readline

N = int(input())
arr = set()

for _ in range(N):
    cmd = input().strip().split()
    
    if cmd[0] == 'add':
        arr.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        arr.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in arr else 0)
    elif cmd[0] == 'toggle':
        num = int(cmd[1])
        if num in arr:
            arr.discard(num)
        else:
            arr.add(num)
    elif cmd[0] == 'all':
        arr = set(range(1, 21))
    elif cmd[0] == 'empty':
        arr = set()

'''
sys.stdin.readline()으로 입력받는 것이 더 빠르고
if list(arr).count(n): 매번 set을 list로 변환을 할 경우 O(N)이라 느리다.
set은 원래 In연산이 O(1)이라 n in arr로 조회를 하면 된다.
check에서 결과값을 출력할 때 한 번에 결과를 담아서 출력하는 것이 더 빠르다
그리고 all로 입력받을 때를 넣지 않았는데
set(1~20)을 넣음으로써 불필요한 연산이나 메모리 누수가 되지 않게 수정하였다.
'''