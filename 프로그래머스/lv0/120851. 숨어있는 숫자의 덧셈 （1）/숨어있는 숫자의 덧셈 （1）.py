def solution(my_string):
    ans = 0
    for char in my_string:
        if char.isdigit():
            ans += int(char)
    return ans