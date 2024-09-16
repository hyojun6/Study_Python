n = input()
a = int(n, 16)
for _ in range(1, 17):
    num = a * _
    h = _
    hex = int(h, 16)
    print("%c"%n + "*%s="%hex + "%s" % hex(num))