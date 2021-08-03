
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))


second_arr = deque()

cnt = 1
start = 0
final_end = 0


while True:
    if len(second_arr) != 0:
        print(f'second_arr가 비지않았을때 : {second_arr}')
        arr = second_arr
        second_arr = deque()
        cnt += 1
    print(f'arr크기 : {len(arr)} , second크기 :{len(second_arr)}')
    ccc = 0
    for a in range(len(arr)):
        ccc += 1
        print('------------',ccc,'-------------')
        start = arr[0][0]
        end = arr[0][1]
        print(f'start값 : {start} , end값 : {end}')
        if final_end <= start:
            cnt += 1
            final_end = end
        else:
            second_arr.append((start, end))
            print(f'second_arr배열 : {second_arr}')
        if ccc == 5:
            break
    if ccc == 5:
        break
    if len(second_arr) == 0:
        print("여기서 걸림")
        break

print(cnt)



