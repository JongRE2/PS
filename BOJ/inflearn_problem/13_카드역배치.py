arr = list()
for i in range(0, 21):
    arr.append(i)

for i in range(10):
    a, b = map(int, input().split())
    pos = 0
    for j in range(a, (a+b)//2 + 1):
        arr[j], arr[b-pos] = arr[b-pos], arr[j]
        pos += 1

for i in range(1, 21):
    print(arr[i], end=' ')