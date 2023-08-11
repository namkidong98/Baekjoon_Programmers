def solution(s):
    s = s.split() #공백으로 구분된 원소들이 리스트의 원소로 들어감
    ans = 0; prev = 0
    for char in s:
        if char.isnumeric(): #0과 양의 정수인 경우
            ans += int(char)
            prev = int(char)
        elif char.startswith('-'): #음의 정수인 경우
            ans += int(char)
            prev = int(char)
        else: #'Z'인 경우
            ans -= prev
    return ans
    