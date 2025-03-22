tarr = []
for i in range(9):
    arr = input()
    tarr.append(arr)
max = 0
posX = 0
posY = 0

for i in range(9):
    arr = tarr[i].split(' ')
    for j in range(len(arr)):
        if max<= int(arr[j]):
            max = int(arr[j])
            posX = i+1
            posY = j+1
print(max)
print(posX, posY)