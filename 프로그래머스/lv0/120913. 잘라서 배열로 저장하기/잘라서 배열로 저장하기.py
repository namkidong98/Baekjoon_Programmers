def solution(my_str, n):
    ans = [] # 빈 리스트 만들기
    i = 0
    while i < len(my_str):
        ans.append(my_str[i : i + n])
        i += n
    return ans