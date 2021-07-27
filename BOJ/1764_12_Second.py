# 듣보잡
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

arr1 = set()
arr2 = set()

for _ in range(a):
    arr1.add(input())

for _ in range(b):
    arr2.add(input())

sum_set =list(arr1.intersection(arr2))
sum_set.sort()

print(len(sum_set))
for a in sum_set:
    print(a,end='')
