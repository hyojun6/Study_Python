n = input()
a = int(n, 16)
for i in range(1,16):
    num = a * i
    hex_num = hex(num)[2:].upper()
    hex_i = hex(i)[2:].upper()
    print(f"{n.upper()}*{hex_i}={hex_num}" )