import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

# 1. 산술평균
mean = round(sum(nums) / n)

# 2. 중앙값
nums.sort()
median = nums[n // 2]

# 3. 최빈값
count = Counter(nums)
mode_freq = count.most_common()  # [(값, 빈도)]
max_freq = mode_freq[0][1]
modes = [num for num, freq in mode_freq if freq == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]  # 두 번째로 작은 값

# 4. 범위
range_val = nums[-1] - nums[0]

# 출력
print(mean)
print(median)
print(mode)
print(range_val)

'''
내 코드에서는 시간초과 오류가 발생했다.
for i in range(len(s_arr)):
    cn = arr.count(s_arr[i])
arr.count()로 빈도값을 구할 때 시간을 많이 사용하는 것 같다
시간초과를 해결하기 위해서는 2가지 방법이 있는데
1.collections.Counter 사용
count = Counter(arr)
mode_freq = count.most_common()
max_freq = mode_freq[0][1]
modes = [num for num, freq in mode_freq if freq == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

count = Counter(arr)
-->arr안의 숫자들이 몇 번씩 나왔는지 세어줍니다.
-->리스트의 각 요소들은 (값,빈도수)튜플입니다.
mode_freq = count.most_common()
-->빈도순으로 정렬된 리스트를 반환합니다.
max_freq = mode_freq[0][1]
-->최대빈도값 저장
modes = [num for num, freq in mode_freq if freq == max_freq]
-->최대빈도값과 빈도 값이 같을 경우 modes에 저장
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]
-->정렬 한 다음 길이가 1일 경우 첫번째 값, 그렇지 않을 경우 두번째 값을 출력

2.빈도수를 저장할 배열을 만들어서 사용
# 최빈값 (수의 범위: -4000 ~ 4000 → 인덱스 0 ~ 8000 사용)
freq = [0] * 8001  # 인덱스: num + 4000

for num in arr:
    freq[num + 4000] += 1

max_freq = max(freq)

modes = []
for i in range(8001):
    if freq[i] == max_freq:
        modes.append(i - 4000)

# 최빈값이 여러 개일 경우 두 번째로 작은 값
mode = modes[0] if len(modes) == 1 else modes[1]

'''