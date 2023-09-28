def solution():
    str = input()
    return 1 if str == str[::-1] else 0
print(solution())