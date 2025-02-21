'''
보이어무어법:
패턴의 끝 문자에서 시작하여 앞쪽을 향해 검사를 수행한다
보이어무어법 알고리즘도 각각의 문자를 만났을 때 패턴을 이동할 크기를 저장하는 표를 미리 만들어 둘 필요가 있다.

패턴에 포함되지 않는 문자를 만난 경우
패턴 이동량은 패턴 문자열의 길이

패턴에 포함되는 문자를 만난 경우
마지막에 나오는 위치의 인덱스가 k이면 이동량은 패턴문자열의 길이 -K -1

*마지막에 나오는 위치의 인덱스
패턴 내에 특정문자가 가장 마지막에 등장하는 위치
abac에서 c:3, b:1 a:2이다 a의 가장 마지막 위치가 2이므로

'''

def bm_match(txt:str,pat:str)->int:
    skip = [None]*256
    
    #건너뛰기 표만들기
    for pt in range(256):
        skip[pt]=len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])]= len(pat)-pt-1
        
    #검색하기
    while pt <len(txt):
        pp = len(pat)-1
        while txt[pt]==pat[pp]:
            if pp==0:
                return pt
            
            pt -=1
            pp -=1
        
        pt +=skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) -pp else len(pat) -pp
        
    return -1

txt = 'ababcdefgha'
pat = 'abc'

idx = bm_match(txt,pat)

print(idx)