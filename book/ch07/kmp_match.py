'''
텍스트와 패턴 안에서 겹치는 문자열을 찾아내 검사를 다시 시작할 위치를 구하여 패턴의 이동이 되도록이면 크게 하는 알고리즘
이 알고리즘은 복잡할 뿐 보이어무어법 보다 성능 면에서 같거나 오히려 낮은 수준이라 실제 프로그래밍에서 많이 사용되지 않는다.

'''

def kmp_match(txt:str, pat:str)->int:
    pt = 1
    pp = 0
    skip = [0]*(len(pat)+1)
    
    skip[pt]=0
    while pt != len(pat):
        if pat[pt]==pat[pp]:
            pt+=1
            pp+=1
            skip[pt] = pp
        elif pp ==0:
            pt+=1
            skip[pt]=pp
        else:
            pp=skip[pp]
    
    #문자열 검색하기
    pt=pp=0
    while pt!= len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt +=1
            pp +=1
        elif pp == 0:
            pt +=1
        else:
            pp = skip[pp]
    
    return pt -pp if pp ==len(pat) else -1

    
        