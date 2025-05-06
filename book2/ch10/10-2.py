#10-1에서 사용한 find함수를 최적화한 코드

def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def find_parent2(parent,x):
    if parent[x] != x:
        parent[x] = find_parent2(parent,parent[x])
    return parent[x]

'''
find_parent2처럼 수정하면 각 노드에 대하여 find함수를 호출한 이후에,
해당 노드의 루트 노드가 바로 부모노드가 된다.
'''
