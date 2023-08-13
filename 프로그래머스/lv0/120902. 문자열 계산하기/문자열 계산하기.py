def solution(my_string):
    my_string = my_string.split()
    i = 1
    ans = int(my_string[0])
    while i + 2 <= len(my_string):
        operator = my_string[i]
        operand = my_string[i+1]
        if operator == '+':
            ans += int(operand)
        else:
            ans -= int(operand)
        i += 2
    return ans