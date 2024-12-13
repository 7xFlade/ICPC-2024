for __ in range(int(input())):
  m, c = map(int, input().split())
  categories = []
  for _ in range(c):
    n = int(input())
    lst = list(map(int, input().split()))
    categories.append(lst)
  
  dp = [c + 1] * (m + 1)
  dp[0] = 0
  ans = -1

  for i in range(c):
    temp_dp = dp.copy()
    for j in range(len(categories[i])):
      for k in range(m, -1, -1):
        if k - categories[i][j] >= 0:
          temp_dp[k] = min(temp_dp[k], 1 + dp[k - categories[i][j]])
          if temp_dp[k] == c: ans = max(ans, k)
    # print(dp)
    dp = temp_dp.copy()  
    # print(dp)
  print(ans)