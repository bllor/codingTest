import sys
input = sys.stdin.readline

cmd = input()
if cmd.count('-')==0:
    print(sum(list(map(int,cmd.split('+')))))
else:
    r_cmd = list(cmd.replace('-',' ').split(' '))
    # print(r_cmd)
    tn = 0
    for i in range(len(r_cmd)):
        if i==0:
            tn=sum(list(map(int,r_cmd[i].split('+'))))
        else:
            tn-=sum(list(map(int,r_cmd[i].split('+'))))
    print(tn)    

