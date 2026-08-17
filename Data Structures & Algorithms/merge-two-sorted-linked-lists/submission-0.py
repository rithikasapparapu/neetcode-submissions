# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
            second = list2
        else:
            head = list2
            second = list1
        first = head
        prev = None

        while first and second:
            if first.val <= second.val:
                prev = first
                first = first.next
            else:
                prev.next = second
                prev = second
                second = second.next
                prev.next = first
        if not first:
            prev.next = second
        return head


        
        




        
        

            


        