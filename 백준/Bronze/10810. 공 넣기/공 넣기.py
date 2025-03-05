N, M = map(int, input().split())
l = [0] * N
for i in range(M):
    start, end, num = map(int, input().split())
    for ii in range(start-1, end):
        l[ii] = num
print(*l)