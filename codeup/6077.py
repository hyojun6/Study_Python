a = int(input())
sum=0
for _ in range(0, a+1):
    if(_%2 == 0):
        sum = sum+_
print(sum)