N = int(input())
# N = 500
t = 1
for i in range(1,N+1):
    # print(i)
    t*=i
# print(t)

# print(str(t)[0])
i=0
# print(str(t)[-1-i])
while True:
    if str(t)[-1-i]!='0':
        # print('if')
        break
    else:
        # print('else')
        i+=1
print(i)    