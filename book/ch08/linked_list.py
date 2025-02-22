#포인터로 연결리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    
    def __init__(self, data:Any = None, next:Node=None):
    #전달 받은 data와 next를 해당 필드에 대입한다.
        self.data = data
        self.next = next
    
class LinkedList:
    
    def __init__(self) -> None:
        self.no = 0 # 리스트에 등록되어있는 노드의 개수
        self.head = None # 머리에 대한 참조
        self.current = None # 현재 주목하고 있는 노드에 대한 참조, 주목포인터
        
    def __len__(self) -> None:
        return self.no

    def search(self, data:any)->int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt +=1
            ptr = ptr.next
        return -1

    def __contains__(self,data:Any)->bool:
        return self.search(data)>=0
    
    def add_first(self, data:Any)->None:
        ptr = self.head
        self.head = self.current = Node(data,ptr)
        self.no +=1
        
    def add_last(self, data:Any):
        if self.head is None: #리스트가 비어있으면
            self.add_first(data) #맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data,None)
            self.no +=1
            
    def remove_first(self)->None:
        #머리노드(가장 첫 번째 노드)를 제거
        if self.head is not None: #리스트가 비어 있으면
            self.head = self.current = self.head.next
        self.no -=1
    
    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head #스캔중인 노드
                pre = self.head #스캔중인 노드의 앞쪽 노드
                
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None #pre는 삭제 뒤 꼬리 노드
                self.current  = pre
                self.no -=1
    
    #임의의 노드를 삭제하는 함수
    def remove(self,p:Node)->None:
        #노드 P를 삭제 
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr= self.head
                
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -=1
    
    def remove_current_node(self)->None:
        self.remove(self.current)
    
    def clear(self)->None:
        
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0
    
    #주목 노드를 한 칸 뒤로 이동
    def next(self)->None:
        if self.current is None or self.current.next is None:
            return False # 이동할 수 없음
        self.current = self.current.next
        return True

    def print_current_node(self)->None:
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)
        
    def print(self)->None:
        ptr =self.head
        
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
    
    
    '''
    이터러블 객체는 원소를 1개씩 꺼내는 구조의 객체이다.
    이터러블 객체를 내장함수인 iter()함수에 인수로 전달하면 그 객체에 대한 이터레이터를 반환합니다.
    이터레이터는 데이터가 줄지어 늘어선 것을 표현하는 객체 입니다.
    이터레이터의 next함수를 호출하거나, 내장함수인 next()함수에 반복자를 전달하면 줄지어 늘어선 원소를 순차적으로 꺼냅니다.
    꺼낼 원소가 없으면 stopIterration예외처리를 합니다.
    '''
    def __iter__(self)-> LinkedListIterator:
        return LinkedListIterator(self.head)

class LinkedListIterator:
    
    def __init__(self, head:Node):
        self.current = head
    
    def __iter__(self)->LinkedListIterator:
        return self

    def __next__(self)->Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data