import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*(n+1)

def dfs(s):
    for i in graph[s]:
        if ans[i] == 0:
            ans[i] = s
            dfs(i)
dfs(1)
for i in ans[2:]:
    print(i)