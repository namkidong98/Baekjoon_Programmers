def solution(babbling):
    result = 0
    possible = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for pos in possible:
            # 빈칸을 안 띄우면 줄어든 글자끼리 붙은 것이 possible의 원소와 일치할 수 있음
            word = word.replace(pos, ' ') 
        if word.strip() == '': # 띄운 빈칸들을 고려해서 좌우 공백을 없애고 빈 string이면
            result += 1
            
    return result

# 정규 표현식을 사용한 아래 풀이가 좋은 것 같다.
# ^는 시작, $는 끝, +는 괄호 안의 요소가 한번 이상 반복됨을 의미
# import re

# def solution(babbling):
#     regex = re.compile('^(aya|ye|woo|ma)+$')
#     cnt=0
#     for e in babbling:
#         if regex.match(e):
#             cnt+=1
#     return cnt
