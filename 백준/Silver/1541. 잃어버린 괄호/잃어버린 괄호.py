equation = input().split('-')

total = sum(map(int, equation[0].split('+'))) # 첫번째 피연산자를 대입하고 시작
for part in equation[1:]: # 다음 피연산자부터
    x = map(int, part.split('+')) # +를 기준으로 내부의 피연산자를 분리하고 정수로 변환
    total -= sum(x) # 합쳐서 total에서 뺀다
        
print(total)
