# 1987번 알파벳
from collections import deque
import sys
R, C = map(int, input().split())
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [list(input().rstrip()) for _ in range(R)]
chk = [0]*26

dq = deque()

def is_valid_coor(y, x):
    return 0 <= y <= R-1 and 0 <= x <= C-1

dq.append((0, 0, 1))
chk[ord(board[0][0]) - ord('A')] = 1
max_cnt = 0

while dq:
    tmp = dq.popleft()
    print(f'좌표 : {tmp[0]},{tmp[1]} -> {board[tmp[0]][tmp[1]]} , 중복카운트 : {tmp[2]} , 최대값 : {max_cnt} ')
    for i in range(4):
        yy = tmp[0] + dy[i]
        xx = tmp[1] + dx[i]
        cnt = tmp[2]
        # print("그냥cnt : ", cnt)
        max_cnt = cnt if max_cnt < cnt else max_cnt

        if is_valid_coor(yy, xx) and (chk[ord(board[yy][xx])-ord('A')] == 0):
            chk[ord(board[yy][xx]) - ord('A')] = 1
            cnt += 1
            # print("2그냥cnt : ", cnt)
            dq.append((yy, xx, cnt))
        else:
            continue
print(max_cnt)