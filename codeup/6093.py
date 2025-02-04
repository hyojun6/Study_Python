f = int(input())
num = list(map(int, input().split())) 
print(' '.join(map(str, num[::-1]))) 