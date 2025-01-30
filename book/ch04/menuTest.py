from enum import Enum

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료']) # menu라는 enum클래스를 만들고, 그 클래스를 menu에 저장

def select_menu()->Menu:
    s = [f'({m.value}){m.name}' for m in Menu] 
    while True:
        print(*s, sep =' ', end='')
        n = int(input(': '))
        if 1<=n <=len(Menu):
            return Menu(n)


# menu = select_menu()
# print("메뉴",menu)

s = ['1','2','3']
print(*s,sep='|') # sep는 구분자
print(s)

'''
for문에서 value를 주지 않았는데 왜 value가 있고 푸시가 1을 갖는지?
--> enum클래스에서 []안의 값은 자동으로 value를 갖는다.
*s는 무엇인지?
--> 리스트의 요소를 문자열로 변환
1을 입력 시 왜 menu.푸시가 출력되는지?
-->menu클래스에서 1에 해당되는 값이 출력됨
'''