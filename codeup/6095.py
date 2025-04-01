pan = [[0] * 19 for _ in range(19)]
i = int(input())
for _ in range(i):
    x, y = map(int, input().split())
    pan[x-1][y-1] = 1
for row in pan: 
    print(' '.join(map(str,row)))