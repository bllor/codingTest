'''
서로소 집합을 활용한 사이클 판별방법
서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다는 특징을 가지고 있다.
알고리즘 순서
1.각 간선을 확인하며 두 노드의 루트 노드를 확인한다
1-1. 루트 노드가 서로 다르다면 두 노드에 대하여 union연산을 수행한다
1-2. 루트 노드가 서로 같다면 사이클이 발생한 것이다
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

'''

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a

#노드의 개수와 간선의 개수를 입력받기
# v,e = map(int, input().split(' '))
v,e = 3,3
parent = [0]*(v+1) # 부모테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

#사이클 발생 여부
cycle = False

arr=['1 2','1 3','2 3']
for i in range(e):
    a,b = map(int,arr[i].split(' '))
    #사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle=True
        break
    #사이클이 발생하지 않았다면 합집합 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클이 발생하였습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
    