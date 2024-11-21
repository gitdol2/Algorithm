# 행렬 덧셈
import sys

N, M = map(int, input().split())
A = []
B = []
R = []

for i in range(N):
    A.append(list(map(int, input().split())))
for j in range(N):
    B.append(list(map(int, input().split())))
for k in range(N):
    row = [] # 행을 하나씩 저장해야 하므로 초기화
    for t in range(M):
        row.append(int(A[k][t])+int(B[k][t]))
    R.append(row)
for row in R:
    print(" ".join(map(str, row))) # 출력 형식 유의