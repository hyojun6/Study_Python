pan = [[0] * 100 for _ in range(100)]
x0,y0 = map(int, input().split())
for i in range(x0):
    pan[i] = [0] * y0
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d==0:
        for j in range(l):
            pan[x-1][y-1+j] = 1        
    elif d==1:
        for j in range(l):
            pan[x-1+j][y-1] = 1
for i in range(0, x0):
    for j in range(0, y0):
        print(pan[i][j], end=' ')
    print('')