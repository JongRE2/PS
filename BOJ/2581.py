a = int(input())
b = int(input())

arr = [True]*10001
sum = 0
min = 2147483647
arr[1] = False
for i in range(2,b+1):
    for j in range(i * i, b + 1, i):
        if (arr[j] == True) and (j <= b):
            arr[j] = False

for i in range(a,b+1):
    if (arr[i] == True):
        sum += i
        if i < min:
            min = i
if sum != 0:
    print(sum)
    print(min)
else:
    print(-1)


