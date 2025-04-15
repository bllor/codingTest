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
    
##############
'''
dic = {
    '-':0,'(':2
}

print(dic['-'])
이렇게 딕셔너리로 key,value로 넣어서 관리하는 것이 더 편했을 것 같다.
나는 
dic = [{'-':0}]이런 식으로 사용하려 했는데, 딕셔너리로 만들지 못했다.    
'''