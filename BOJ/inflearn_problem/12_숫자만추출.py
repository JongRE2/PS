import math
str = input()

sum = 0
for a in str:
    if a >= '0' and a <= '9':
        sum *= 10
        sum += int(a)
cnt = 0
for i in range(1, int(math.sqrt(sum))+1):
    if sum % i == 0:
        cnt += 2
print(sum)
print(cnt)

