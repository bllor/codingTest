# [답지]
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
    '''
    word = dz=z=일 때
    croatia의 배열이 0번부터 진행하면서 word와 일치하는 배열을 찾는다.
    croatia[0]= 'c='로 word와 일치하지 않아서 치환되지 않고, 다음 번호로 넘어가며
    croatia[2]= 'dz='는 word내에 있으므로 *로 대체되어 word=*dz가 된다.
    croaita[7]= 'z='는 word내에 있으므로 *로 대체되어 word = **가 된다.
    word의 길이는 2이므로 2가 출력된다.
    '''  
print(len(word))



# str = input()

# # str = 'ddz=z='

# n = 0 

# for i in range(len(str)):
#     if i == len(str)-1:
#         continue
#     else:        
#         if i == len(str)-2:
#             if str[i-1]+str[i]+str[i+1]=='dz=':
#                 continue
#             str2 = str[i]+str[i+1]
#             if str2 =='c=' or str2=='c-' or str2=='d-' or str2=='lj' or str2 =='s=' or str2=='z=' or str2=='nj':
#                 n+=1
#         else:
#             str2 = str[i]+str[i+1]
#             str3 = str[i]+str[i+1]+str[i+2]
#             if str3=='dz=':
#                 n+=2
#                 continue
#             elif str2 =='c=' or str2=='c-' or str2=='d-' or str2=='lj' or str2 =='s=' or str2=='z=' or str2=='nj':
#                 n+=1
# print(len(str)-n)