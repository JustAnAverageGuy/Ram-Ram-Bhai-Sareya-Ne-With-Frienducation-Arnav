# https://www.codingninjas.com/studio/problems/rod-cutting-problem_800284

import sys;input=sys.stdin.readline

from functools import cache

W = []

@cache
def dp(n):
    if n == 0: return 0
    return max(dp(n-i-1) + W[i] for i in range(n))

def solve():
    n = int(input())
    dp.cache_clear()
    global W
    W = list(map(int,input().strip().split()))
    print(dp(n))



for _ in range(int(input())): solve()
