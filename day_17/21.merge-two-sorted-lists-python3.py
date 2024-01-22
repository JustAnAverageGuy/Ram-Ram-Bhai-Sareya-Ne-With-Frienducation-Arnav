# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):  return list1
        if not (list1 and list2): return list1 or list2 # short circuit
        seek, target = sorted([list1, list2], key=lambda x: x.val) # choose head
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val: seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head

# @leet end
