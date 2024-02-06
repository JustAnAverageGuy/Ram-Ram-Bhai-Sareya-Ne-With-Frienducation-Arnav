# https://www.codingninjas.com/studio/problems/0-1-knapsack_920542
from os import *
from sys import *
from collections import *
from math import *

import sys;input=sys.stdin.readline

from functools import cache
n,W,V,capacity = -1,[],[],-1

@cache
def dp(i,w):
    if i < 0: return 0
    if w <= 0: return 0
    if w >= W[i-1]:
        return max(dp(i-1, w), dp(i-1, w - W[i-1])+V[i-1])
    return dp(i-1,w)

def solve():
    dp.cache_clear()
    global n, W, V, capacity
    n = int(input())
    W = list(map(int,input().strip().split()))
    V = list(map(int,input().strip().split()))
    capacity = int(input())
    print(dp(n-1, capacity))
    
for _ in range(int(input())): solve()
