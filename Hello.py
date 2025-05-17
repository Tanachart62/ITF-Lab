print("hello word")
x = int(input())
for i in range(x):
    for j in range(i):
        for k in range(j*2):
            print("/")
        print("*")