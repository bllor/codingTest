N = int(input())
arr = [None]*N
for i in range(N):
    arr[i] = input()

# arr=[
# '(())())',
# '(((()())()',
# '(()())((()))',
# '((()()(()))(((())))()',
# '()()()()(()()())()',
# '(()((())()(',    
# ]

for ch in arr:
    stack =[]
    is_Balance=True
    for i in range(len(ch)):
        # print(stack)
        if ch[i] == ')':
            if len(stack)>0 and stack[-1]=='(' :
                # print('pop')
                stack.pop()
            else:
                # print('e')
                is_Balance=False
                break
        else:
            stack.append(ch[i])
            
    if len(stack)==0 and is_Balance:
        print('YES')
    else:
        print('NO')