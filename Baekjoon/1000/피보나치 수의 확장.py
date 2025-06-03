# 1788 피보나치 수의 확장
# dp(바텀업)을 이용해 음수인 경우의 피보나치 수 구하기
# 피보나치는 n >= 0인 경우를 구하지만 이 문제는 n이 음수인 경우는 어떠한가를 묻는다
# F(1) = F(0) + F(-1)
# F(n) = F(n-1) + F(n-2)을 아래와 같이 바꿔 F(-1)이 어떻게 값이 도출되는 지 확인.
# F(n-2) = F(n) - F(n-1)

# 결국 n >= 0인 경우와 비슷하다. 시작은 결국 n이 0과 1이기에.
# 단지 n < 0인 경우, 절댓값 n이 짝수 or 홀수인지 확인만 해줘야한다.

dp = [0] * 1000003

n = int(input())
MOD = 1000000000

dp[0] = 0
dp[1] = 1

for i in range(2, abs(n)+1):
  dp[i] = (dp[i-1] + dp[i-2]) % MOD

if n < 0: # 음수
  num = abs(n)
  if num % 2 == 0: # 짝수인 경우는 음수임
    print(-1)
  else: # 홀수인 경우는 양수임
    print(1)
  print(dp[num])
elif n == 0:
  print(0)
  print(0)
else:
  print(1)
  print(dp[n])
