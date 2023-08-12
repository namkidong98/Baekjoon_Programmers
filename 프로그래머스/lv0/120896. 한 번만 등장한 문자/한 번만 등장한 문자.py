def solution(s):
    s = list(s) # iterable한 list로 변환
    dic = {} # 빈 딕셔너리 만들기
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
            
    ans = [] # 한 번만 등장하는 문자열을 넣을 빈 리스트 생성
    for char in dic:
        if dic[char] == 1:
            ans.append(char)
    
    return ''.join(sorted(ans))