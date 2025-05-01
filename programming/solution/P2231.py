n = int(input())

x = 0
for i in range(1, n):  # 1부터 n까지 모든 숫자를 탐색
    s = sum(map(int, str(i)))# str(i)를 문자열로 변환 --> 각 자리를 정수로 변환 --> 그 다음 더하기
    if i + s == n:
        x = i
        break

print(x)

#반례사례 : 
# 2일 때는 1+1 = 2 ,18 = 9+9 = 18, 8=4+4가 되므로
# n//2+1의 범위는 잘못 설정되었다.
# n = int(input())
# if n==2:
#     print(1)
# else:    
#     mid = n//2+1
#     x = 0
#     for i in range(mid,n):
#         s = f'{i}'
#         tn =0
#         for j in range(len(s)):
#             tn+=int(s[j])
#         if i + tn ==n:
#             x=i
#             break
        
#     print(x)