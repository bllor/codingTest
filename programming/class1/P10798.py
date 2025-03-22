words = [input().strip() for _ in range(5)]

result = ""
for i in range(15):  # 최대 길이가 15이므로 0~14까지 순회
    for word in words:
        if i < len(word):  # 현재 단어의 길이를 초과하지 않는다면 추가
            result += word[i]

print(result)             
                
                

