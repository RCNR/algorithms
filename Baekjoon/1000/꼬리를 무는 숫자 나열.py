# 꼬리를 무는 숫자 나열.py 1598
# 4칸씩 끊어 놓고 있다는 생각, 인덱싱 처리를 해야된다는 생각

a, b = map(int, input().split())

x1 = (a-1)//4
y1 = (a-1)%4

x2 = (b-1)//4
y2 = (b-1)%4

print(abs(x1-x2) + abs(y1-y2))