# 치킨댄스를 추는 곰곰이를 본 임스.py 25191
# 콜라가 2개 있어야 치킨 1마리를 시킬 수 있다는 조건이기에 콜라부터 계산
# 그 다음 남은 예산으로 치킨을 최대한 시키기 - 맥주는 1개당 치킨 1마리

n = int(input())
a, b = map(int, input().split())

chicken_by_cola = a // 2
ret = min(n, chicken_by_cola)
n = n - ret
print(ret + min(n, b))