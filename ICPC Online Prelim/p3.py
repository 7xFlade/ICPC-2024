for __ in range(int(input())):
  s1, f1, h1, s2, f2, h2, s3, f3, h3 = map(int, input().split())
  totalS = s1 + s2 + s3
  totalF = f1 + f2 + f3
  totalH = h1 + h2 + h3

  ans = (totalS + totalF + totalH, "FHS")
  if totalF - f1 + totalH - h2 + totalS - s3 < ans[0]:
    ans = (totalF - f1 + totalH - h2 + totalS - s3, "FHS")
  if totalF - f1 + totalS - s2 + totalH - h3 < ans[0]:
    ans = (totalF - f1 + totalS - s2 + totalH - h3, "FSH")
  if totalH - h1 + totalF - f2 + totalS - s3 < ans[0]:
    ans = (totalH - h1 + totalF - f2 + totalS - s3, "HFS")
  if totalH - h1 + totalS - s2 + totalF - f3 < ans[0]:
    ans = (totalH - h1 + totalS - s2 + totalF - f3, "HSF")
  if totalS - s1 + totalF - f2 + totalH - h3 < ans[0]:
    ans = (totalS - s1 + totalF - f2 + totalH - h3, "SFH")
  if totalS - s1 + totalH - h2 + totalF - f3 < ans[0]:
    ans = (totalS - s1 + totalH - h2 + totalF - f3, "SHF")

  # print(totalS - s1 + totalF - f2 + totalH - h3, "SFH")
  # print(totalS - s1 + totalH - h2 + totalF - f3, "SHF")
  # print(totalH - h1 + totalS - s2 + totalF - f3, "HSF")
  # print(totalH - h1 + totalF - f2 + totalS - s3, "HFS")
  # print(totalF - f1 + totalH - h2 + totalS - s3, "FHS")
  # print(totalF - f1 + totalS - s2 + totalH - h3, "FSH")
  print(ans[1], ans[0])