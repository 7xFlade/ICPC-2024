for __ in range(int(input())):
  n = int(input())
  s = input()
  t = input()
  revT = t[::-1]

  if s == t:
    print(0)
    continue

  if s == revT:
    print(2)
    continue
  
  m = len(s)
  flag = False

  c = 0
  for i in range(n):
    if s[i] != t[i]:
      c += 1
  m = min(m, c)

  c = 0
  for i in range(n):
    if s[i] != revT[i]:
      c += 1

  if c == m:
    print(m * 2 - 1)
    continue
  
  if c < m:
    m = c
    flag = True

  if flag and m % 2 == 1:
    ans = m * 2
  elif flag and m % 2 == 0:
    ans = m * 2 - 1
  elif not flag and m % 2 == 1:
    ans = m * 2 - 1
  elif not flag and m % 2 == 0:
    ans = m * 2
  print(ans)