# 검증수
N = list(map(int, input().split()))
R = 0
for i in N:
    R += i**2
print(R%10)