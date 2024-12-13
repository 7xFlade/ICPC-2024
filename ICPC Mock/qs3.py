test_cases = int(input())
threshold = int(input())

def is_exceeding(packets,threshold,size):
    for x in range(2,size):
        change1 = abs(packets[x]-packets[x-1])
        change2 = abs(packets[x-1]-packets[x-2])
        if (abs(change1-change2) >= threshold):
            print("1 ", end=" ")
        else:
            print("0 ", end=" ")

    print("")

for x in range(test_cases):
    size = int(input())
    num_packets = list(map(int,input().split()))
    is_exceeding(num_packets,threshold,size)

input = map 