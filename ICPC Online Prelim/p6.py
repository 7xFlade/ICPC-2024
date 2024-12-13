from collections import deque

for __ in range(int(input())):
  n = int(input())
  cnt = {}
  d = {}
  for i in range(n - 1):
    u, v = map(int, input().split())
    cnt[u] = cnt.get(u, 0) + 1
    cnt[v] = cnt.get(v, 0) + 1
    d[u] = d.get(u, []) + [v]

  def bfs(u):
    q = deque()
    q.append(u)
    depth = 0

    while(q):
      depth += 1
      sz = len(q)
      # print(q)
      for i in range(sz):
        cur = q.popleft()
        if cur in d:
          for neigh in d[cur]:
            q.append(neigh)
    return depth
  
  print(bfs(0), *sorted(cnt.values(), reverse=True)[0:2])