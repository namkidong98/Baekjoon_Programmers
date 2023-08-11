def solution(my_string):
    element = list(set(my_string)) # 원소로 있는 문자들을 모아놓음
    ans = ''
    for char in my_string:
        if char in element:
            ans += char
            element.remove(char)
    return ans
    