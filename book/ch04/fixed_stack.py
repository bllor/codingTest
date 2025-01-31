from typing import Any

class FixedStack:
    
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self, capacity: int = 256)->None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self)->int:
        return self.ptr
    
    def is_empty(self)->bool:
        return self.ptr<=0           
    
    def is_full(self)->bool:
        return self.ptr>=self.capacity
    
    def push(self, value:Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self)->Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -=1
        return self.stk[self.ptr]
    
    def peek(self)->Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self)-> None:
        self.ptr = 0
        
    def find(self, value:Any)->Any:
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i]==value:
                return i
        return -1
    
    def count(self, value:Any)->bool:
        c = 0
        for i in range(self.ptr):
            if self.stk[i]==value:
                c+=1
        return c
    
    def __contains__(self,value:Any)->bool:
        return self.count(value)

    def dump(self)->None:
        if self.is_empty():
            print('no data')
        else:
            print(self.stk[:self.ptr]) #0번부터 ptr-1번까지 출력        
            
            
'''
__len()__이나 __contains()__는 다른 함수들과 다르게 정의 되어 있는데
다음과 같이 함수를 정의할 경우, 클래스형의 인스턴스 obj에 대한 __len()__함수를 호출하는
obj.__len()__를 간단히 len(obj)로 사용할 수 있다.

밑줄 2개인 더블 언더스코어를 줄여서 던더라고 한다.

'''