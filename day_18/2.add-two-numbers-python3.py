# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # python can handle 100 digit numbers pretty efficiently
        n1 = []
        n2 = []

        t = l1
        while t:
            n1.append(str(t.val))
            t = t.next
        
        t = l2
        while t:
            n2.append(str(t.val))
            t = t.next
        
        s = int("".join(n1[::-1])) + int("".join(n2[::-1]))
        
        root = n = ListNode(0)
        
        for i in reversed(str(s)):
            val = int(i)
            n.next = ListNode(val)
            n = n.next
        
        return root.next
        
# @leet end

