number = int(input())
cur = 1
while cur <= number:
    if cur + sum(list(map(int,str(cur)))) == number:
        break
    cur += 1

if cur > number:
    print(0)
else: print(cur)