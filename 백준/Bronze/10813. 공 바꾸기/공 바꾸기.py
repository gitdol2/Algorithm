N, M = map(int, input().split())
l = list(range(1, N+1))
for t in range(M):
    i, j = map(int, input().split())
    temp = l[i-1]
    l[i-1] = l[j-1]
    l[j-1] = temp
print(*l)