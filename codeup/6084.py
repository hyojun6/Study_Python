h, b, c, s = map(int, input().split())
bit=(h*b*c*s)/(8*1024*1024)
print("%.1f"%bit + " MB")