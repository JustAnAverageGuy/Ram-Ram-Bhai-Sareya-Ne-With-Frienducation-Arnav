# https://www.codingninjas.com/studio/problems/ceil-from-bst_920464

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    # Write your code here.
    ceil = -1
    curr = root
    while curr is not None:
        if curr.data == x: return x
        if curr.data >  x:
            ceil = curr.data 
            curr = curr.left
        else:
            curr = curr.right
    return ceil
