'''
퀵정렬
배열 [5,7,9,0,3,1,6,2,4,8]가 있다고 가정할 때
1.리스트의 첫번째 항목이 피벗이 된다.
2.이후에 왼쪽에서부터 5보다 큰 데이터를 선택하고, 오른쪽에서부터는 5보다 작은 데이터를 선택하고, 그 다음 둘의 자리를 변경한다.
3.그 다음 피벗보다 작은 데이터를 찾는다.
4.왼쪽에서 오는 값의 위치와 오른쪽에서 오는 값의 위치가 엇갈릴 경우에는 작은 데이터와 피벗을 교체한다.
5.피벗이 이동하게 되면 피벗을 기준으로 왼쪽은 피벗보다 작은 값, 오른쪽은 피벗보다 큰 값이 위치하게 되는데, 이 작업을 분할 혹은 파티션이라고 한다.
6.왼쪽, 오른쪽 리스트에서 1~5번 과정을 반복한다.

*
퀵 정렬은 재귀 함수 형태로 작성하면 구현이 간결해진다.
재귀 함수일 때 퀵 정렬의 끝나는 조건은 리스트의 데이터가 1개인 경우이다.
'''
array  = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start,end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left <=right:
        while left <= end and array[left] <= array[pivot]:
        #피벗보다 큰 데이터를 찾을 때까지 반복
            left +=1
        while right > start and array[right]>=array[pivot]:
        #피벗보다 작은 데이터를 찾을 때까지 반복
            right -=1
        if left> right:
        #왼쪽의 위치와 오른쪽의 위치가 교차하는 경우    
            array[right],array[pivot] = array[pivot],array[right]
        else:
        #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체    
            array[left], array[right] = array[right],array[left]
    
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array, 0, len(array)-1)
print(array)

def python_quick_sort(array):
    if len(array)<=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]
    
    return python_quick_sort(left_side)+[pivot]+python_quick_sort(right_side)

print(python_quick_sort(array))