# https://www.codingninjas.com/studio/problems/subset-sum-equal-to-k_1550954


from functools import cache

A = []

@cache
def dp(i, remaining):
    if i < 0: return False
    if remaining in [A[i],0]: return True
    return dp(i-1, remaining) or ((remaining - A[i] > 0) and dp(i-1, remaining - A[i]))


def subsetSumToK(n, k, arr):
    global A
    dp.cache_clear()
    A = arr[::]
    return dp(n-1, k)
