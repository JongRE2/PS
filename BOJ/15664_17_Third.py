# N과 M(10)

from itertools import combinations

n, m = map(int, input().split())

arr = list(map(int, input().split()))

results = list()

for i in combinations(arr, m):
    if sorted(i) not in results:
        results.append(sorted(i))

results.sort()
print(results)
for i in results:
    print(' '.join(map(str, i)))


