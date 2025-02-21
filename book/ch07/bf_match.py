'''
부루트 포스법 : 선형 검색을 단순하게 확장한 알고리즘라서 단순 법이라고도 합니다.

'''

def bf_match(txt:str, pat:str)->int:
    pt = 0 #txt를 따라가는 커서
    pp = 0 #pat를 따라가는 커서
    
    while pt != len(txt) and pp != len(pat):
        if txt[pt]== pat[pp]:
            pt+=1
            pp+=1
        else:
            pt = pt -pp+1
            pp = 0
    
    return pt -pp if pp == len(pat) else -1


    