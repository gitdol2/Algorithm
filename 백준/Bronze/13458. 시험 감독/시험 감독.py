# 시험 감독
import math
N = int(input()) # 시험장 수
A = list(map(int, input().split())) # 시험장별 응시자 수
B, C = map(int, input().split()) # 총감, 부감
proctor_total = 0

for i in range(N):
    if A[i]>B: # 총감독관만으로는 학생 전부 커버 못하는 경우
            proctor_assistant = math.ceil((A[i]-B)/C)
            proctor_total += 1 + proctor_assistant
    else: # 총감독관으로만 학생 전부 커버 가능한 경우
        proctor_total += 1
print(proctor_total)