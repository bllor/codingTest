
N = int(input())
arr1 = [None]*N


for i in range(N):
    arr1[i] = input()


arr2 = list(set(arr1))
arr2.sort(key=lambda x: (len(x),x))

for text in arr2:
    print(text)