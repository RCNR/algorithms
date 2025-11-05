# 9996 한국이 그리울 땐 서버에 접속하지
# '*' 기준으로 앞, 뒤로 나눠서 각 문자열마다 비교 -> 슬라이싱 사용, 맨끝에 비교할 때 endswith사용해도 O => string.endswith(back)
import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
ary = list(input().rstrip() for _ in range(n))

part = s.split('*', 1) # '*' 기준으로 1번만 분리
front = part[0]
back = part[1]

for i in range(len(ary)):
  string = ary[i]
  if front == string[:len(front)] and back == string[-len(back):] and len(s)-1 <= len(string):
    print("DA")
  else:
    print("NE")
