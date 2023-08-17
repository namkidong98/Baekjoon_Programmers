def solution(s):
    i = 0; ans = 0
    if len(s) == 1:
        return 1
    
    while i < len(s): # 길이가 적어도 2이상
        std = s[i] # 첫 단어를 기준으로 삼는다
        cnt = 1; # 기준이 되는 숫자가 나온 횟수 - 다른 숫자가 나온 횟수
        i += 1 # 다음 인덱스로 이동
        while i < len(s):
            if s[i] == std:
                cnt += 1
            else:
                cnt -= 1
            i += 1
            if cnt == 0:
                break
        ans += 1
    return ans