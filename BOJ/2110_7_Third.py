# 공유기 설치
import sys
input = sys.stdin.readline

def route_count(val):
    cur_house = house[0]
    count = 1
    for i in range(1,n):
        if cur_house + mid <= house[i]:
            count += 1
            cur_house = house[i]
    return count


n, c = map(int, input().split())
house = list()
for _ in range(n):
    house.append(int(input()))
house.sort()

left = 0
right = house[-1] - house[0]
result = 0
while left <= right:
    mid = (left + right) // 2

    if route_count(mid) >= c:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)
