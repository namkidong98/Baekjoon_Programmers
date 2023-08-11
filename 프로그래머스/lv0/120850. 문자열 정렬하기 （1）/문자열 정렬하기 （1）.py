def solution(my_string):
    numbers = []
    for num in range(10):
        numbers.append(str(num))
    ans = []
    for char in my_string:
        if char in numbers:
            ans.append(int(char))
    return sorted(ans)