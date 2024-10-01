arr = [[0]*10 for _ in range(10)]
for i in range(10):
    arr[i] = list(map(int, input().split()))
    
x=1
y=1
while(1):      # 2일때 이동할수없을때
    if(arr[x][y] == 2):
        arr[x][y] = 9
        break
    
    if(arr[x][y+1] == 1):
        if(arr[x+1][y] == 1):
            arr[x][x] = 9
            break
        else:
            arr[x][y] = 9
            x += 1
    else:
        arr[x][y] = 9
        y += 1
print('\n'.join(' '.join(map(str, row)) for row in arr))