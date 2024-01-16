def count_painters(boards, max_len):
    n = len(boards)
    totalSum = 0
    painters = 1
    for i in range(n):
        totalSum += boards[i]
        if (totalSum > max_len):
            totalSum = boards[i]
            painters += 1
    return painters

def findLargestMinDistance(boards, k):
    l = max(boards)-1
    r = sum(boards)+1
    while (r-l > 1):
        m = l + (r - l) // 2
        if ( count_painters(boards, m) <= k):
            r = m
        else:
            l = m
    return r

