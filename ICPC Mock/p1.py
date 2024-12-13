for __ in range(int(input())):
  m, c = map(int, input().split())
  dp, catg = [], []
  for i in range(c):
    dp.append([0] * (m + 1))
    n = int(input())
    catg.append(list(map(int, input().split())))
  
  for i in catg[0]:
    dp[0][i] = 1

  for i in range(c):
    for j in catg[i]:
      for k in range(m):
        if dp[i - 1][k] == 1 and k + j <= m:
          dp[i][k + j] = 1
  
  flag = False
  for i in range(m, -1, -1):
    if dp[-1][i] == 1:
      print(i)
      flag = True
      break
  if not flag:
    print(-1)