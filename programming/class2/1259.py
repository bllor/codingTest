arr =[]
q = 0
while True:
     a = int(input())
     if a==0:
          break
     else:
          arr.append(a)
     
# print(arr)
arr2= [True]*len(arr)
for i in range(len(arr)):
     # print(arr[i])
     str = f'{arr[i]}'
     numberLength = len(str)
     midNumber= numberLength//2   
     for j in range(midNumber):
          if str[j] != str[numberLength-j-1]:
               arr2[i]=False
               break

for i in range(len(arr2)):
     if arr2[i]:
          print('yes')
     else:
          print('no')     
     
     
     
     
     # if numberLength%2==0:
     #      midNumber= numberLength//2   
     #      print('mid',midNumber)
     #      for i in range(midNumber):
     #           print('s1',i,'s2',numberLength-i-1)
     # else:
     #      midNumber= numberLength//2
     #      print('mid',midNumber)
     #      for i in range(midNumber):
     #           print('s1',i,'s2',numberLength-i-1)
          