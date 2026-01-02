# 제곱수의 합.py 1699
# 제곱수의 합으로 표현하는 방법은 여러 가지가 있을 수 있음을 주의
# n = (어떤 수둘의 합) + i^2 -> 여기서 i^2은 여러 개가 올 수 있음
# 따라서 dp[i] = min(dp[i], dp[i - j*j] + 1) 형태로 점화식을 세워야 함

n = int(input())

dp = [i for i in range(n+1)] # 1^2 최대 개수로 초기화

for i in range(1, n+1):
  idx = 1

  while idx * idx <= i:
    dp[i] = min(dp[i], dp[i - idx * idx] + 1)
    
    idx += 1
print(dp[n])