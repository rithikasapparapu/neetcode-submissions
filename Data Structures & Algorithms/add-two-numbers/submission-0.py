# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        carry = 0
        prev = None
        while first and second:
            res = int(first.val + second.val) + carry
            first.val = res % 10
            carry = res // 10
            prev = first
            second = second.next
            first = first.next
        while first:
            res = int(first.val) + carry
            first.val = res % 10
            carry = res // 10
            prev = first
            first = first.next
        while second:
            res = int(second.val) + carry
            second.val = res % 10
            carry = res // 10
            prev.next = second
            prev = second
            second = second.next
        if carry > 0:
            node = ListNode(carry)
            prev.next = node
        return l1



        