# 25305
n, m = map(int, input().split())
student = list(map(int, input().split()))

student.sort(reverse=True)
print(student[m-1])