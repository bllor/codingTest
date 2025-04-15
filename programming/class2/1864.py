arr= ['-','\\','(','@','?','>','&','%','/']
valueArr = [0,1,2,3,4,5,6,7,-1]

str=''
while str!='#':    
    str=input()
    tn = 0
    if str=='#':
        break
    for i in range(len(str)):
        for j in range(len(arr)):
            if str[i]==arr[j]:
                tn +=valueArr[j]*(8**(len(str)-1-i))
                break
    print(tn)