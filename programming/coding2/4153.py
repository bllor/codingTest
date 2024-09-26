while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    lst.sort()
    if lst[2]**2 == lst[0]**2 + lst[1]**2:  # 피타고라스 정리 활용
        print('right')
    else:
        print('wrong')



# 입력값중에 어떤 수가 가장클지 모른다는 것이 틀린점

# t = True
# while(t):
#     a,b,c = map(int, input().split(' '))
#     if a==0 and b==0 and c == 0:
#         t = False
#         break
    
#     if c**2 ==(a**2+b**2):
#         print('right')
#     else:
#         print('wrong')

    