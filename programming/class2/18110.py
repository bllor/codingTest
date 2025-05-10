N= int(input())
arr = [None]*N
if N==0:
    print(0)
else:
    for i in range(N):
        arr[i] = int(input())
    except_number = round(N*0.15)
    arr.sort()
    arr1 = []

    for i in range(N):
        if i>=except_number and i<=(N-except_number-1):
            arr1.append(arr[i])
    tn =0
    for i in arr1:
        tn+=i
    print(round(tn/len(arr1)))
