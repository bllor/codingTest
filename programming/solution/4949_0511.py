while True:
    line = input()
    if line == '.':
        break

    stack = []
    balanced = True
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print('yes')
    else:
        print('no')

'''
내 코드에서 틀린 이유는
if len(s_arr)==0 and (i==']' or i ==')'):
    is_Balance = False
    break
괄호 배열에 아무값도 없고 닫는 괄호가 있을 때 False가 되도록 코드를 작성하였는데
[)]처럼 닫는 괄호가 처음 나오는게 아니면 ) false가 되지 않는다.
그래서 ]나 )이 나왔을 때 조건문을 사용해야 한다.


include_Arr= ['(',')',']','[']

while True:
    str = input()
    if str == '.':
        break
    filterArr = []
    for i in range(len(str)):    
        if str[i] in include_Arr:
            filterArr.append(str[i])
    # print(filterArr)

    s_arr=  []
    is_Balance=True;
    for i in (filterArr):
        if len(s_arr)==0 and (i==']' or i ==')'):
            is_Balance = False
            break
        
        if i =='(' or i =='[':
            s_arr.append(i)
        else:
            if i == ']' and len(s_arr)>0 and s_arr[len(s_arr)-1]=='[':
                # print('[]')
                # print(s_arr)
                # s_arr=s_arr[:len(s_arr)-1]
                s_arr.pop()
            if i == ')' and len(s_arr)>0 and s_arr[len(s_arr)-1]=='(':
                # print('(')
                # s_arr=s_arr[:len(s_arr)-1]
                s_arr.pop()

    if is_Balance and len(s_arr)==0:
        print('yes')
    else:
        print('no')
'''
