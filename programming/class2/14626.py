import sys
input = sys.stdin.readline

# cmd = input().rstrip()
cmd = '*788968302053'
star_index = cmd.index('*')
# print(cmd.index('*'))

cmd1 = cmd.replace('*','0')
tn = 0
for i in range(len(cmd1)):
    if i%2:
        tn+=int(cmd1[i])*3
    else:
        tn+=int(cmd1[i])
        
# print(tn)
if star_index%2:
    #홀수
    for i in range(0,10,1):
        if (tn+i*3)%10==0:
            print(i)
            break
else:
    #짝수
    for i in range(0,10,1):
        if (tn+i)%10==0:
            print(i)
            break