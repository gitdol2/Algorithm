# 이상한 기호
def operator(a, b):
    return (a+b)*(a-b)
A, B = map(int, input().split())
print(operator(A, B))