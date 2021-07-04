# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, node = 0, head # shadow copy only copy address 
        while node and count < k: 
            node = node.next
            count += 1
        # we couldn't generate a k size of sub linked list
        if count < k:
            return head
        # after this reverse function, head becomes tail of a linked list and then generate a K size of sublist, which is prev (head)
        new_head, prev = self.reverse(head, count)
        # linked the previous k size of sub linked list tail to the new k size of sub linked list head
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, curr = None, head
        while count > 0:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
            count -= 1
        return curr, prev
           