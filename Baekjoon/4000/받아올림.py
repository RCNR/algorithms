
# 반례: 999 1
# 18번 라인에서 n에게 1을 더 추가하는 방식임 이때 숫자가 9로 끝나면 carry가 일어남
# 그래서 애초에 더 작은놈에게 무조건 적으로 1을 넘기기 위해 11번째 줄에서 swap을 해버려서 더 작은 거에 넘길 수 있게
while(True):
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    cnt = 0

    if n>m:
        n,m = m,n

    for _ in range(max(len(str(n)), len(str(m)))):
        k1 = n % 10
        k2 = m % 10

        n = n / 10
        m = m / 10

        if k1+k2 >= 10:
            n += 1
            cnt += 1
            
    
    print(cnt)
    