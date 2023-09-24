num = int(input())
i = 0
x = 1
while i < num:
    if i == num - 1:
        x = -1
    print(' '*(num-1-i) + '*'*((i+1) * 2 - 1))
    i += x
    if i==-1 :break