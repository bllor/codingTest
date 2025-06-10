count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)

'''
1,2,3,4를 배열에 넣고 4,3을 제거한 다음
5부터 배열에 넣어야 하는데 어떻게 넣어야할지 몰라서 풀지 못함

count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
        
num = 4
while count<=num:
    stack.append(1) op.append('+') count+=1 stack = [1]
    stack.append(2) op.append('+') count+=1 stack = [1,2]
    stack.append(3) op.append('+') count+=1 stack = [1,2,3]
    stack.append(4) op.append('+') count+=1 stack = [1,2,3,4]

if stack[-1] == num:
    4==4-->true:
    stack.pop -->stack=[1,2,3]
    op.append('-')
num = 3
    count>num(=5>3)이므로
    if stack[-1] == num:
    3==3-->true:
    stack.pop -->stack=[1,2]
    op.append('-')

num = 6
while count<=num:
    stack.append(5) op.append('+') count+=1 stack = [1,2,5]
    stack.append(6) op.append('+') count+=1 stack = [1,2,5,6]
if stack[-1]==num:
    6 ==6
    stack.pop --> stack = [1,2,5]
    op.append('-')
num = 8
while count<=num:
    stack.append(7) op.append('+') count+=1 stack = [1,2,5,7]
    stack.append(8) op.append('+') count+=1 stack = [1,2,5,7,8]
if stack[-1]==num:
    8==8
    stack.pop--> [1,2,5,7]
num = 7
if stack[-1]==num:
    7==7
    stack.pop--> [1,2,5]
num = 5
if stack[-1]==num:
    5==5
    stack.pop--> [1,2]
num = 2
if stack[-1]==num:
    2==2
    stack.pop--> [1]
num = 1
if stack[-1]==num:
    1==1
    stack.pop--> [0]
    
'''