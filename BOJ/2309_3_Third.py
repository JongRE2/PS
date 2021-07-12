# 일곱난쟁이
from itertools import combinations

arr = list()

for _ in range(9):
    arr.append(int(input()))

for i in combinations(arr,7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break