# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists):
        head = dummy = ListNode(0)
        heap = [(l.val, l) for l in lists if l]
        heapq.heapify(heap)
        while heap:
            val, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            dummy.next = node
            dummy = dummy.next 
        return head.next 