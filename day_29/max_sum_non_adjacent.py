# https://www.codingninjas.com/studio/problems/maximum-sum-of-non-adjacent-elements_843261

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    
    # modifies nums inplace, so only uses Θ(1) extra space
    if len(nums) < 3: return (max(nums))
    
    max_in_i_2 = nums[0]

    for i in range(2, n):
        nums[i] += max_in_i_2
        max_in_i_2 = max(max_in_i_2, nums[i-1])


    return max(nums[-1], nums[-2])




# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
