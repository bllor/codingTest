#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수와 간선의 개수 입력받기
# v,e = map(int, input().spilt())
v,e= 6,4
parent = [0]*(v+1) #부모 테이블 초기화

#부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

arr = ['1 4', '2 3', '2 4','5 6']    
#union 연산을 각각 수행    
for i in range(e):
    a,b = map(int,arr[i].split(' '))
    union_parent(parent,a,b)

print('각 원소가 속한 집합: ',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

print('부모 테이블 :',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')
    
#이 알고리즘을 사용하게 되면 노드의 개수가 V개이고 find 혹은 union연산의 개수가 M일 때
#전체 시간 복잡도는 O(VM)이 되어 비효율적이다.
    