# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        num = count - n + 1
        temp1 = head
        if num == 1: return head.next
        prev = None
        while temp1:
            if num == 1:
                prev.next = temp1.next
                return head
            prev = temp1
            temp1 = temp1.next
            num -= 1
        