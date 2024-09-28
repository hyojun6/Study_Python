pan = [[0] * 19 for _ in range(19)]

for i in range(19):
    pan[i] = list(map(int, input().split()))

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    for j in range(19):
        pan[x][j] = 1 - pan[x][j]
    
    for j in range(19):
        pan[j][y] = 1 - pan[j][y]

for row in pan:
    print(*row)