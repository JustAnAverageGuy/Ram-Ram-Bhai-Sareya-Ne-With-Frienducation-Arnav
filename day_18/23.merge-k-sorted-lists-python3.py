# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import merge

class Solution:
    def makeGenerator(self, head):
        while head:
            yield head.val
            head = head.next
        return

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # using the merge routine from heapq
        x = merge(*(self.makeGenerator(i) for i in lists))

        root = n = ListNode(0)
        for i in x:
            n.next = ListNode(i)
            n = n.next
        return root.next
# @leet end
