N,M = map(int, input().split(' '))

prime_arr = []
for i in range(N,M+1,1):
    if i ==1:
        continue
    if i ==2:
        prime_arr.append(i)
        continue
    is_p = True
    for pno in prime_arr:
        if i%pno == 0:
            is_p=False
            break
    if is_p:
        prime_arr.append(i)
        

# print(prime_arr)            

for number in prime_arr:
    print(number)
            
        