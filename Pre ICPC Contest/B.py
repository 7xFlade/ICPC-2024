for __ in range(int(input())):
  n = int(input())
  p = list(map(int, input().split()))

  ans = 3

  for i in range(n):
    if i + 1 == p[p[i] - 1]:
      ans = 2
      break

  print(ans)