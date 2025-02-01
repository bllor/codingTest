from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

def select_menu()->Menu:
    s= [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='', end='')
        n = int(input(': '))
        if 1 <=n <= len(Menu):
            return Menu(n)


s = FixedStack(64)

while True:
    print(f'현재 데이터의 개수 : {len(s)}/{s.capacity}')
    menu = select_menu()
    
    if menu == Menu.푸시:
        x = int(input('데이터를 입력하시오'))
        try:
            s.push(x)
        except FixedStack.Full:
            print('가득찼다.')
    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('Empty Stack')
    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f' peek data is {x}')
        except FixedStack.Empty:
            print('stack is Empty')
    elif menu == Menu.검색:
            x = int(input('검색할 값을 입력하시오.'))
            if x in s:
                print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다. ')
            else:
                print('no data')
    elif menu == Menu.덤프:
        s.dump()
    else:
        print('종료')
        break
        