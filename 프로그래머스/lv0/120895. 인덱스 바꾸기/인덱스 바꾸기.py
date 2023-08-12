def solution(my_string, num1, num2):
    ans = my_string[:num1]
    ans += my_string[num2]
    ans += my_string[num1 + 1 : num2]
    ans += my_string[num1]
    ans += my_string[num2 + 1: ]
    return ans