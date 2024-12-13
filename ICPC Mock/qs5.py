map1 = list(input().split())
map2 = list(input().split())
lenmap1 = len(map1)
dic = dict()

def checker(dic, str1, str2):    
    print(len(str1), len(str2))
    if ((len(str1) >= 20 or len(str1) <= 3) or (len(str2) >= 20 or len(str2) <= 3)):
        return "No"
    else:
        lenstr2 = len(str2)
        for i in range(lenstr2):
            if (str1[i] == str2[i]):
                continue
        while str1[i] != str2[i]:
            if str1[i] in dic:
                for x in dic[str1[i]]:
                    str1[i] = x
                    if str2[i] == str1[i]:
                        break
            else:
                return  "No"
    return "Yes"

for i in range(lenmap1):
    if map1[i] in dic:
        dic[map1[i]].append(map2[i])
    else:
        dic[map1[i]] = [map2[i]]
while(True):
    a = input()
    if (len(a) == 0):
        break
    string = list(a.split())
    str1 = []
    str2 = []
    for y in string[0]:
        str1.append(y)
    for y in string[1]:
        str2.append(y)
    print(checker(dic, str1, str2))
    
