# 최단경로
import heapq, sys

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())

adj = [[] for _ in range(v)]

for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u-1].append((v-1, w))


def dijkstra(src):
    distance = [INF] * v
    distance[src] = 0
    pq = [] # min heap으로 리스트
    heapq.heappush(pq, (distance[src], src))

    while pq:
        min_dist, here_node = heapq.heappop(pq)

        if distance[here_node] < min_dist:
            continue

        for there_node, d in adj[here_node]:




