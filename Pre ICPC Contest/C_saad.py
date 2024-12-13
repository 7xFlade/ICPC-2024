for __ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))

  l = 1
  r = 1

  for i in range(1, n):
    if a[i] == a[i - 1]:
      l += 1
    else:
      break
  
  for i in range(n - 2, -1, -1):
    if a[i] == a[i + 1]:
      r += 1
    else:
      break
  
  if a[0] == a[-1]:
    print(max(0, n - l - r))
  else:
    print(max(0, n - max(l, r)))