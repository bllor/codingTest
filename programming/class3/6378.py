while True:
    value  = input()
    if value =='0':
        break
    
    while True:
        arr = []
        for i in range(len(value)):
            arr.append(int(value[i]))
        if sum(arr)<10:
            print(sum(arr))
            break
        else:
            value = str(sum(arr))
        