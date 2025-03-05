num = int(input())
for i in range(1, num+1):
    print(" "*(num-i) , end = "")
    print("*"*(num-(num-i)))