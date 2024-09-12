a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
if((a<b) & (a<c)):
    print(a)
elif((b<a) & (b<c)):
    print(b)
else:
    print(c)