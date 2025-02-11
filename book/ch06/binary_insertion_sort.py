from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence)->None:
    n = len(a)
    for i in range(1,n):
        key = a[i]
        pl=0
        pr = i-1
        
        while True:
            pc =(pl+pr)//2
            print('pc',pc,'||',f'{(pl+pr)//2} ||pl:{pl}||pr:{pr}')
            if a[pc]==key:
                break
            elif a[pc]< key:
                pl = pc+1
            else:
                pr = pc-1
            if pl >pr:
                print(f'break pl{pl}>pr{pr}')
                break
        
        pd = pc+1 if pl<=pr else pr+1
        print('pd, pc, pl, pr',pd, pc, pl, pr)    
        
        print('i',i,'pd',pd)
        for j in range(i,pd,-1):
            print(f'a[{j}]=a[{j-1}]')
            a[j]=a[j-1]
        a[pd] = key
        print('-------')

if __name__ =='__main__':
    x=[6,4,3,7,1]
    binary_insertion_sort(x)
    
    for i in range (len(x)):
        print(x[i], end=' ')                