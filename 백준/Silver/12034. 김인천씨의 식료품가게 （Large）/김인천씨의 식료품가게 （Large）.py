# 김인천씨의 식료품가게 (Large)
T = int(input())
for t in range(T):
    N = int(input())
    P = list(map(int,input().split()))
    R = []
    P.reverse()
    i = 0
    while i < len(P):
        j = 0
        while j < len(P):
            if P[i]*0.75 == P[j]:
                R.append(P[j])
                del P[j]
                break
            j += 1
        i += 1
    R.reverse()
    print(f"Case #{t+1}: ", end = '')
    print(' '.join(map(str,R)))