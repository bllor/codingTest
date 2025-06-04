N = int(input())
M = int(input())

arr =[None]*M

for i in range(M):
    arr[i] = input()
b_arr= [1]
for i in range(M):
    computer,conn = map(int,arr[i].split(' '))
    if computer in b_arr :
        b_arr.append(conn)
    
    if conn in b_arr:
        b_arr.append(computer)
print(b_arr)
print(len(set(b_arr))-1)