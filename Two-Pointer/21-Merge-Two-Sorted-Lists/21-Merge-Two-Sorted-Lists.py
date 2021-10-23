# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        l3 = ListNode()
        dummy = l3
        
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next 
                l1 = l1.next 
            else:
                dummy.next = l2
                dummy = dummy.next 
                l2 = l2.next 
        
        dummy.next = l1 if l1 else l2
        
        return l3.next 