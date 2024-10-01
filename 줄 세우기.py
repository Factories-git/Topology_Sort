from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
indegree = [0] * (n+1)
a = [[] for i in range(n + 1)]

for i in range(m):
    s,e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=' ')

    for nxt in a[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
