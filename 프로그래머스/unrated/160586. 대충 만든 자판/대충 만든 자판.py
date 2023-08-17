def solution(keymap, targets):
    dic = {} # 빈 딕셔너리 만들기
    for i in keymap:
        for char in i:
            if char not in dic: # 해당 글자가 딕셔너리에 없으면
                dic[char] = i.index(char) + 1 # 새로 추가
            else: # 해당 글자가 딕셔너리에 있다면
                if dic[char] > (i.index(char) + 1): # 기존 딕셔너리의 값보다 작으면
                    dic[char] = i.index(char) + 1 # 갱신
    # 모든 keymap을 분석하여 글자들의 최소 횟수를 딕셔너리에 저장한 상태
    
    ans = []
    for target in targets:
        total = 0
        for char in target:
            click = dic.get(char, -1) # 딕셔너리에 없는 경우
            if click == -1:
                total = -1
                break;
            total += click
        ans.append(total)
                             
    return ans