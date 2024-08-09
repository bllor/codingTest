x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
d = (x1-x2)**2+(y1-y2)**2
print('YES' if (r1+r2)**2>d else 'NO')

# x1,y1,i1 = map(int, input().split(' '))
# x2,y2,i2 = map(int, input().split(' '))


# r1xs = (x1-i1)
# r1ys = (y1-i1)
# r1xf = (x1+i1)
# r1yf = (y1+i1)


# r2xs =(x2-i2)
# r2ys= (y2-i2)
# r2xf =(x2+i2)
# r2yf= (y2+i2)



# if r1xs <=r2xs and r1xf>=r2xf:
#     if r1ys <=r2ys and r1yf>=r2yf:
#         print("YES")
#     else:
#         print("NO")
# elif r2xs <=r1xs and r2xf>=r1xf:
#     if r2ys <=r1ys and r2yf>=r1yf:
#         print("YES")
#     else:
#         print("NO")
# elif r1ys <=r2ys and r1yf>=r2yf:
#     if r1xs <=r2xs and r1xf>=r2xf:
#         print("YES")
#     else:
#         print("NO")
# elif r2ys <=r1ys and r2yf>=r1yf:
#     if r2xs <=r1xs and r2xf>=r1xf:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")
         
# # if r1xs <=r2xs and r1xf>=r2xf or r2xs <=r1xs and r2xf>=r1xf or r1ys <=r2ys and r1yf>=r2yf or r2ys <=r1ys and r2yf>=r1yf:
# #     print("YES")
# # else:
# #     print("NO")

# # r11 = x1-i1
# # r12 = y1+i1

# # r21 = x2-i2
# # r22 = y2-i2

# # if r11 == r21 and r12 == r22:
# #     print("NO")
# # else:
# #     if r11<r22 or r21<r12:
# #         print("NO")
# #     else:
# #         print("YES")


# # n = 0
# # m = 0
# # t = 1

# # l = [-2,-1,0,1,2]
# # # for i in range(n-t,m+t+1):
# # #     print(i)
    
# # s = [i for i in range(n-t,m+t+1)]

# # print(set(l)-set(s))
# # aa = set(l)-set(s)
# # bb = set(s)-set(l)



# # x1,y1,r1 = map(int, input().split(' '))
# # x2,y2,r2 = map(int, input().split(' '))

# # t1 = [i for i in range(x1-r1,y1+r1+1)]    
# # t2 = [i for i in range(x2-r2,y2+r2+1)]

# # min1 = min(list(t1))
# # max1 = max(list(t1))
# # min2 = min(list(t2))
# # max2 = max(list(t2))
# # if min1>=min2:
# #     if max1<=max2:
# #         print("YES")
# #     else:
# #         print("NO")
# # else:
# #     if max1>=max2:
# #         print("YES")
# #     else:
# #         print("NO")
    
          