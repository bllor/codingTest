# 틀린 이유 : 학점을 곱해주지 않음
r2 = []
for i in range(3):
    r = input().split(' ')[2].strip()
    r2.append(r)

r3 = []
pf =0
for i in range(len(r2)):
    if r2[i] == 'A+':
        r3.append(4.5)
    elif r2[i]== 'A0':
        r3.append(4.0)
    elif r2[i]== 'B+':
        r3.append(3.5)
    elif r2[i]== 'B0':
        r3.append(3.0)
    elif r2[i]== 'C+':
        r3.append(2.5)
    elif r2[i]== 'C0':
        r3.append(2.0)
    elif r2[i]== 'D+':
        r3.append(1.5)
    elif r2[i]== 'D0':
        r3.append(1.0)
    elif r2[i]== 'F':
        r3.append(0)
    
    else:
        r3.append(99)
        pf+=1
r3 = [r3[i] for i in range(len(r3)) if r3[i] != 99 ]
print(sum(list(r3))/len(r3))