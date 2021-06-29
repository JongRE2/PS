import sys

arr = [True]*100001

a = int(input())
b = int(input())
sum = 0
min = sys.maxsize
for i in range(1,10001):
    if i//2 == 0:
        arr[i] = False

for i in range(3,b+1,2):
    if arr[i] == True:
        for j in range(i*i,b+1,i):
            arr[j] = False

for i in range(a,b+1):
    if arr[i] == True:
        sum += i
        if arr[i] <= min:
            min = i


print(-1) if sum == 0 else print(sum)
print(min)
