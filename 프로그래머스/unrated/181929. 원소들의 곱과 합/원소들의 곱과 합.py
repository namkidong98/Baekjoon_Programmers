def solution(num_list):
    prod = 1
    for i in num_list:
        prod *= i
    
    return 1 if prod < sum(num_list) ** 2 else 0