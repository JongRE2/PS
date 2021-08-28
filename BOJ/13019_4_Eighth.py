# A를 B로
from collections import Counter

num1 = list(input())
num2 = list(input())
if Counter(num1) != Counter(num2):
    print(-1)
else:
    i = len(num1)-1
    j = len(num2)-1
    count = 0
    while i >= 0:
        if num1[i] == num2[j]:
            j -= 1
        else:
            count += 1
        i -= 1
    print(count)


