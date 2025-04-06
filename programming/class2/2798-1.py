n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()  # 정렬 (O(n log n))
max_sum = 0

# 첫 번째 카드 선택
for i in range(n - 2):
    left, right = i + 1, n - 1  # 투 포인터 초기화

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if total > m:
            right -= 1  # 합이 m보다 크면 큰 숫자를 줄이기
        else:
            max_sum = max(max_sum, total)
            left += 1  # 합이 m 이하이면 left 증가

print(max_sum)