# 시간표짜기
import sys
input = sys.stdin.readline
subjects = []


n = int(input())

for _ in range(n):
    _, *t = map(int, input().split())
    subject = 0
    for i in t:
        subject |= (1 << i)
    subjects.append(subject)


m = int(input())

for _ in range(m):
    cnt = 0
    _, *q = map(int, input().split())
    student = 0
    for i in q:
        student += (1 << i)
    for classes in subjects:
        if classes == (student & classes):
            cnt += 1
    print(cnt)
