n = int(input())
for i in range(1, n+1):
    a = int(i)%10
    if a==3 or a==6 or a==9:
        print('X', end=' ')
    else:
        print(i, end=' ')