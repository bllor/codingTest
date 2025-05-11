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
    
    for i in (filterArr):
        print(s_arr)
        if len(s_arr)==0 and (i==']' or i ==')'):
            s_arr.append(i)
            break
        
        if i =='(' or i =='[':
            s_arr.append(i)
        else:
            if i == ']' and len(s_arr)>0 and s_arr[len(s_arr)-1]=='[':
                # print('[]')
                # print(s_arr)
                s_arr=s_arr[:len(s_arr)-1]
            if i == ')' and len(s_arr)>0 and s_arr[len(s_arr)-1]=='(':
                # print('(')
                s_arr=s_arr[:len(s_arr)-1]

    if len(s_arr)==0:
        print('yes')
    else:
        print('no')
            