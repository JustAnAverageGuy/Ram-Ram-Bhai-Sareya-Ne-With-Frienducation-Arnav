# https://www.codingninjas.com/studio/problems/allocate-books_1090540
def num_studs(arr, n , pages):
    stu = 1
    sm = 0
    for i in range(n):
        if (sm + arr[i] <= pages): sm += arr[i]
        else:
            stu += 1
            sm = arr[i]
    return stu




def findPages(arr: [int], n: int, m: int) -> int:

    if (m > n) : return -1
    l = max(arr)-1
    r = sum(arr)+1
    while (r-l) > 1:
        mid = (r+l)//2
        if ( num_studs(arr, n, mid) > m ):
            l = mid
        else:
            r = mid
    return r

