def solution(numbers, k):
    x = 1
    while( (x * len(numbers) / 2) < k):
        x+=1
    numbers = numbers * x
    numbers = numbers[::2]
    return numbers[k-1]