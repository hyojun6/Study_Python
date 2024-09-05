a, b, c = map(int, input().split(' '))
print(a+b+c, end=' ')
print("{:.2f}".format(((float(a)+float(b)+float(c))//3)))