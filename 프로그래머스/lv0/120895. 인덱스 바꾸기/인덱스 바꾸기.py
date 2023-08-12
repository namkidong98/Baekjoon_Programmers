def solution(my_string, num1, num2):
    my_string = list(my_string) # iterable object로 변경
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1] # 자리 변경
    ans = ''.join(my_string)
    return ans