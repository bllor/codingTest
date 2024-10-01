s = input()

arr = [0 for i in range(26)]
for i in range(len(s)):
    arr[ord(s[i])-97]+=1

print(str(arr).replace('[','').replace(']','').replace(',',''))