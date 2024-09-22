n = [0] * 24
a = int(input())
num_list = list(map(int, input().split()))
for num in num_list:
    n[num] += 1
print(' '.join(map(str, n[1:24])))