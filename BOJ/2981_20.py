# 검문

import math

arr = list()
count = int(input())

for i in range(count):
    val = int(input())
    arr.append(val)

arr.sort(reverse=True)
small_val = arr.pop()
arr.append(small_val)
small_val_range = int(math.sqrt(small_val))+1

remainder = -1
for i in range(count):
    for j in range(2,small_val_range):
        if remainder == -1:


