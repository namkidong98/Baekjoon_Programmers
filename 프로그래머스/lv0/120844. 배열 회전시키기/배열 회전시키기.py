def solution(numbers, direction):
    if direction == 'right':
        a = numbers.pop()
        numbers.insert(0, a)
    else: #left인 경우
        a = numbers[0]
        numbers.remove(a)
        numbers.append(a)
    return numbers