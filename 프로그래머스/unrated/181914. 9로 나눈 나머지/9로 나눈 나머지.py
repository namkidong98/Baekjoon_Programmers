def solution(number):
    number = list(number)
    return sum([int(digit) for digit in number]) % 9
    
        