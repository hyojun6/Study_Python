a, b, c = map(int, input().split())
n = 0
for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            print(i, j, k)
            n+=1
print(n)