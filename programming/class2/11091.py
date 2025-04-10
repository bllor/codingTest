strArr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input())
inputArr = ['None']*n
for i in range(n):
    inputArr[i]=input()

for i in range(n):
    arr = [0]*26
    inputStr = inputArr[i]
    # inputStr = 'a b C !'
    str1= inputStr.replace(' ','')
    for i in range(len(str1)):
        s1 = str1[i].lower()
        n1 = ord(s1)-97
        if n1<0:
            continue
        else:
            arr[n1]+=1
    str2=[]
    for i in range(len(arr)):
        if arr[i]== 0:
            str2.append(strArr[i])
    if len(str2)==0:
        print('pangram')
    else:
        print('missing', ''.join(str2))  
    