# 회사에 있는 사람

import sys

input = sys.stdin.readline

st = set()

for _ in range(int(input())):
    name, situation = input().split()
    if situation == 'enter':
        st.add(name)
    else:
        if name in st:
            st.remove(name)


for val in sorted(st, reverse=True):
    print(val)


