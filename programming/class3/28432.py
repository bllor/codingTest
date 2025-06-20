'''
내 코드는 인덱스 에러가 발생하였는데
맨 끝에 ?가 올 경우 처리가 되지 않은 것 같다.
'''
import sys
N = int(sys.stdin.readline())
arr =[sys.stdin.readline().rstrip() for i in range(N)]
CN = int(sys.stdin.readline())
c_arr =[sys.stdin.readline().rstrip() for i in range(CN)]
empty_idx = arr.index('?')
h_idx = 0
t_idx = 0
h_able = True
t_able = True
if empty_idx==0:
    h_able=False
elif empty_idx==N-1:
    t_able= False
h_idx = int(empty_idx)-1 
t_idx = int(empty_idx)+1
h_str = arr[h_idx][len(arr[h_idx])-1] if h_able else ''#물음표 앞 글자의 마지막 
t_str = arr[t_idx][0] if t_able else '' #물음표 뒤글자의 처음

# print(h_str,t_str,h_able,t_able)
for c_str in c_arr:
    if not h_able:
        if c_str[len(c_str)-1]==t_str:
            if c_str not in arr:
                print(c_str)
                break
    elif not t_able:
        if c_str[0] == h_str:
            if c_str not in arr:
                print(c_str)
                break
    else:    
        if c_str[0] == h_str and c_str[len(c_str)-1]==t_str:
            if c_str not in arr:
                print(c_str)
                break