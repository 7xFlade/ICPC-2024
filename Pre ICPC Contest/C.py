def make_equal(a, n):
    dic =  dict()
    for x in a:
        if(x in dic):
            dic[x] += 1
        else:
            dic[x] = 1
            
    max_count = 0
    max_key = 0
    new_count  = 0
    for key in dic:
        if(dic[key] > max_count):
            max_count = dic[key]
            max_key = key
    print(max_key) 
         
    while (dic[max_key] != n): # while not all elements are equal to max_key
        for z in range(n):
            if(a[z] != max_key): # find the first element that is not equal to max_key
                i = z # i is the index of the first element that is not equal to max_key
                break 
        for z in range(i, n): 
            if(a[z] == max_key): # find the first element that is equal to max_key after i
                j = z # j is the index of the first element that is equal to max_key after i
                break
        new_count += j - i # update the number of operations needed
        for z in range(i, j):
            a[z] = max_key # make all elements between i and j equal to max_key
            dic[max_key] += 1 # update the count of max_key     
            
    print(a)
    return new_count # return the number of operations needed to make all elements equal to max_key
    
num = int(input())
for i in range(num):
    n = int(input())
    a = list(map(int, input().split()))
    count = make_equal(a, n)
    print(count)