a, b = map(int, input().split())

x1 = (a-1)//4
y1 = (a-1)%4

x2 = (b-1)//4
y2 = (b-1)%4

print(abs(x1-x2) + abs(y1-y2))