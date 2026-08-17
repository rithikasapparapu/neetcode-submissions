# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = second = head
        if not head or not head.next:
            return None
        p = None
        while second and second.next:
            p = first
            first = first.next
            second = second.next.next
        p.next = None
        prev = None
        while first:
            temp = first.next
            first.next = prev
            prev = first
            first = temp
        first = head
        prev1 = None
        while first:
            if not first.next:
                prev1 = first
            temp = first.next
            temp1 = prev.next
            first.next = prev
            prev.next = temp
            first = temp
            prev = temp1
        if prev:
            prev1.next.next = prev



