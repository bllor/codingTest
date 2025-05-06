str= input()

s_arr = list(set(str))
n_arr = [0]*len(s_arr)

for i in range(len(str)):
    for j in range(len(s_arr)):
        if s_arr[j] == str[i]:
            n_arr[j]+=1

e = 0
o = 0
for num in n_arr:
    if num%2 ==0:
       e+=1
    else:
        o+=1

if e>0 and o>0:
    print('0/1')
elif e>0:
    print(0)
else:
    print(1)
         
