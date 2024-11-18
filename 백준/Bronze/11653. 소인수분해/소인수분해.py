num = int(input())
i = 1
while i < num:
    i += 1
    if num%i == 0:
        print(i)
        num //= i
        i = 1