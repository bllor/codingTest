n = int(input())
s, m , l, x, x2, x3 = map(int,input().split(' '))
t, p = map(int, input().split(' '))

tt = 0
# if s%t != 0:
#     tt +=(s//t)+1
# else:
#     tt+=s//t

# if m%t != 0:
#     tt +=(m//t)+1
# else:
#     tt+=m//t

# if l%t != 0:
#     tt +=(l//t)+1
# else:
#     tt+=l//t

# if x%t != 0:
#     tt +=(x//t)+1
# else:
#     tt+=x//t

# if x2%t != 0:
#     tt +=(x2//t)+1
# else:
#     tt+=x2//t

# if x3%t != 0:
#     tt +=(x3//t)+1
# else:
#     tt+=x3//t

# 각 값을 t로 나눈 몫과 나머지를 활용하여 필요한 개수를 계산
tt = sum((val + t - 1) // t for val in [s, m, l, x, x2, x3])

print(tt)
    
tp =0
tp = n//p
trp = n%p

print(tp,trp)
