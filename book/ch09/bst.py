'''
이진트리:노드가 왼쪽 자식과 오른쪽 자식만 갖는 트리

노드를 채우는 방법
1)마지막 레벨을 제외한고 모든 레벨은 노드가 가득 차 있습니다.
2)마지막 레벨에 한해서 왼쪽부터 오른쪽으로 노드를 채우되 반드시 끝까지 채우지 않아도 됩니다.

이진검색 트리의 조건
1)왼쪽 서브트리 노드의 키값은 자신의 노드 키값보다 작아야 합니다
2)오른쪽 서브트리 노드의 키값은 자신의 노드 키값보다 커야 합니다.

이진검색트리는 다음과 같은 특징이 있어서 알고리즘에서 폭 넓게 사용되고 있습니다
- 구조가 단순합니다
- 중위 순회의 깊이 우선 검색을 통하여 노드값을 오름차순으로 얻을 수 있습니다
- 이진 검색과 비슷한 방식으로 아주 빠르게 검색할 수 있습니다.
- 노드를 삽입하기 쉽습니다.
'''

from __future__ import annotations
from typing import Any,Type

class Node:
    def __init__(self, key:Any, value:Any, left:Node=None,right:Node=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    
    def __init__(self):
        self.root  = None #루트
        
    def search(self, key:Any)->Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key==p.key:
                return p.value
            elif key <p.key:
                p = p.left # 왼쪽 트리에서 검색
            else:
                p = p.right # 오른쪽 트리에서 검색
                
    def add(self, key:Any, value: Any)->bool:
        
        def add_node(node: Node, key: Any, value: Any)->None:
            #node를 루트로 하는 서브트리에 키가 key이고, 값이 value인 노드를 삽입
            if key==node.key:
                return False
            elif key <node.key:
                if node.left is None:
                    node.left = Node(key,value,None,None)
                else:
                    add_node(node.left,key,value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None,None)
                else:
                    add_node(node.right,key,value)
            
            return True
        
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key,value)
        
    def remove(self,key:Any)->bool:
        '''
        자식노드가 한 개일 경우 : 삭제되는 위치에 자식노드를 배치
        자식노드가 2개 일 경우 : 제거하는 노드의 왼쪽 서브트리에서 가장 큰 값을 배치
        '''
        p = self.root
        parent = None
        is_left_child = True
        
        while True:
            if p is None: # 키가 존재하지 않다는 뜻
                return False
            
            if key == p.key: #key와 노드의 p의 키가 같은 경우
                break
            else:
                parent = p #가지를 내려가기 전에 부모를 정함
                if key < p.key: #key가 작으면 왼쪽자식으로 내려감
                    is_left_child=True
                    p = p.left
                else:
                    is_left_child=False
                    p = p.right
                
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root :
                self.root = p.left
            elif is_left_child:
                parent.left = p.left  # 부모 포인터가 왼쪽 자식을 가르킴
            else:
                parent.right = p.left # 부모 포인터가 오른쪽 자식을 가르킴
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
                
            p.key  = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left

        return True
    
    
    def dump(self, reverse=False)->None:
        
        def print_subtree(node:Node):
            #node를 루트로하는 서브트리의 노드를 키의 오름차순으로 출력
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)
        
        print_subtree(self.root)
    
        def print_subtree_rev(node:Node):
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)
        
        print_subtree_rev(self.root) if reverse else print_subtree(self.root)
                