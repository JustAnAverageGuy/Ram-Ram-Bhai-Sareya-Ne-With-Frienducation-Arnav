# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        tmp = head
        while tmp.next is not None:
            tmp = tmp.next
            cnt += 1
        tmp = head
        for i in range(cnt//2):
            tmp = tmp.next
        return tmp

# @leet end
